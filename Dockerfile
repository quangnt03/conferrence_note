FROM python:3.11-bullseye
WORKDIR /usr/src
RUN apt upgrade -y && apt update -y
RUN apt install -y ffmpeg
COPY . /usr/src
CMD ["pip", "install", "-r", "requirements.txt"]
EXPOSE 8080
RUN python app.py