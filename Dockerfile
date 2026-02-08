FROM python:3.11-slim
WORKDIR /backend
COPY . .
CMD ["python", "main.py"]