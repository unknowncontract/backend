FROM python:3.11.5-alpine as production

WORKDIR /app

COPY *.py .

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]