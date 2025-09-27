FROM python:3.12-alpine

# Установка curl для healthcheck
RUN apk --no-cache add curl

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

ENV PORT=5001

EXPOSE 5001

CMD ["python", "app.py"]
