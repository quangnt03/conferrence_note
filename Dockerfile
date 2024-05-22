FROM python:3.10-slim

WORKDIR /code 
COPY ./requirements.txt /code/requirements.txt

RUN apt update && apt upgrade -y && apt install ffmpeg -y
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", " 0.0.0.0", "--port", "8080", "--reload"]