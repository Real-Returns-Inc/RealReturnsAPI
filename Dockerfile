FROM python:3.9

WORKDIR /code

RUN pip install --no-cache-dir --upgrade fastapi uvicorn requests

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8067"]