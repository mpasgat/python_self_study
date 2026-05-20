FROM python:3.11-slim

WORKDIR /app
COPY day4_fastapi/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY day4_fastapi/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]