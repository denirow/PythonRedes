FROM python:3.10.0a6-buster

WORKDIR /opt/robotframework/

COPY src /opt/robotframework/
RUN mkdir /opt/robotframework/results

RUN apt-get update \
   && apt-get install -y xvfb wget ca-certificates fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 \
   libatspi2.0-0 libcups2 libdbus-1-3 libgbm1 libgtk-3-0 libnspr4 libnss3 \
   libxcomposite1 libxkbcommon0 libxrandr2 xdg-utils ntpdate openssl

RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
   && dpkg -i google-chrome*.deb \
   && rm google-chrome*.deb

RUN python3 -m pip install robotframework \
   && pip install robotframework-requests \
   && pip install robotframework-seleniumlibrary \
   && pip3 install webdrivermanager

RUN webdrivermanager chrome