FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY /counter_service_app .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python", "counter-service.py"]