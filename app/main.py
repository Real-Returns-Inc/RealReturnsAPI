import os
import sys

from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

import requests

origins = [
    "http://localhost:8000"
    "http://localhost",
    "http://localhost:8080",
    "https://staging.roi.realreturns.ai"
    "https://roi.realreturns.ai"
]

attomd_base = "https://api.gateway.attomdata.com/propertyapi/v1.0.0"

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]



# Ensure all required environment variables are set
try:  
  RENTOMETER_API_KEY = os.environ['RENTOMETER_KEY']
except KeyError: 
  print('[error]: `RENTOMETER_KEY` environment variable required')
  sys.exit(1)

try:  
  ATTOM_API_KEY = os.environ['ATTOM_KEY']
except KeyError: 
  print('[error]: `ATTOM_KEY` environment variable required')
  sys.exit(1)


headers = {
    'Accept': 'application/json',
    'apikey': ATTOM_API_KEY,
    'accept': 'application/json',
}

app = FastAPI(middleware=middleware)

@app.get("/rent_deets/")
async def read_item(latitude: float = 40.016870, longitude: float = -105.279620, bedrooms: int = 2, look_back_days: int = 90, building_type: str = "house"):
    res = requests.get(f"https://www.rentometer.com/api/v1/summary?api_key={RENTOMETER_API_KEY}&latitude={latitude}&longitude={longitude}&bedrooms={bedrooms}&look_back_days={look_back_days}&building_type={building_type}")
    while "errors" in res.json():
        look_back_days += 90
        res = requests.get(f"https://www.rentometer.com/api/v1/summary?api_key={RENTOMETER_API_KEY}&latitude={latitude}&longitude={longitude}&bedrooms={bedrooms}&look_back_days={look_back_days}&building_type={building_type}")
    return res.json()

@app.get("/property_deets/")
async def get_property_details(address: str, bedrooms: int = 2, building_type: str = "house"):
    params = (
        ('address', address),
    )
    if building_type == "apartment":
        params = (
            ('address', address), # Maybe specify apartment in the future
        )
    res = requests.get(f"{attomd_base}/property/expandedprofile",
            headers=headers,
            params=params
        )
    return res.json()
