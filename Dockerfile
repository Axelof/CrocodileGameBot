FROM python:3.11.3-alpine

ENV PROJECT_DIR=/CrocodileGameBot
WORKDIR $PROJECT_DIR

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# CHANGE TO "CMD ["uvicorn", "server:app"]"
CMD ["python", "src"]