
FROM python:3.9-slim

WORKDIR /app
COPY ./src /app/src
# RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "/app/src/main.py"]