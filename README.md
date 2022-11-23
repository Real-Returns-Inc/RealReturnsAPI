# RealReturns API

Wrappers around a few different APIs in the Real Estate Market.

## Setting Up

Make sure you have python3 installed

```bash
python3 -m pip install fastapi uvicorn
```

### Environment Variables

The following environment variables need to be set and this can be done by adding this to your `.bash_profile` or `.zshrc`

```
export RENTOMETER_KEY="dsgfsdfsdf-sdfsdfdsf"
export ATTOM_KEY="sdfsdfsdfdsfsdfsdfsdfsdfsdf"
```

## Running the Server

```bash
uvicorn app.main:app --reload --port 8067
```