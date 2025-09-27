FROM python:3.12-alpine

# Установка curl для healthcheck
RUN apk --no-cache add curl

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

ENV PORT=5002
ENV GENERATOR_URL=http://microservice1:5001

EXPOSE 5002

CMD ["python", "app.py"]
