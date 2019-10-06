FROM ubuntu:latest
MAINTAINER xuboxiao "xuboxiao55@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3 python3-dev python3-pip
RUN mkdir /app
COPY app.py /app
COPY Dockerfile /app
COPY models.py /app
COPY requirements.txt /app
COPY service.py /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["./app.py"]