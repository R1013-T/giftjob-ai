FROM python:3.11.1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./ ./

# CMD ["bash", "-c", "cd ./src && uvicorn main:app --reload --host 0.0.0.0 --port 8001"]