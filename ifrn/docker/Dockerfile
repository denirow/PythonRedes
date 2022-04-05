FROM debian:latest
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install nginx net-tools nano iputils-ping systemctl curl -y
RUN systemctl start nginx