FROM python:3.11.5-alpine as production

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY src/ src/

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]