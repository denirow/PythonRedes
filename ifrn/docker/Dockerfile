FROM nginx:latest
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install net-tools nano iputils-ping curl -y
WORKDIR /usr/share/nginx/html/
COPY index.html .