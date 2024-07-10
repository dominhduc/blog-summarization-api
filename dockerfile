FROM python:3.8-slim

RUN pip install flask transformers

COPY . /app
WORKDIR /app

CMD ["python", "app.py"]
