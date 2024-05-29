FROM python:3.10-slim

WORKDIR /usr/src/
COPY . /usr/src/

RUN pip install --no-cache-dir --upgrade -r /usr/src/requirements.txt

EXPOSE 80

ENTRYPOINT [ "uvicorn", "--host", "0.0.0.0", "--port", "80", "app.main:app" ]