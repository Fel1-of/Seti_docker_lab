FROM python:3.13.0-alpine3.20

WORKDIR app

# Если не сработает, попробовать вернуть http://
RUN echo https://mirrors.dotsrc.org/alpine/v3.20/main > /etc/apk/repositories \
  && echo https://mirrors.dotsrc.org/alpine/v3.20/community >> /etc/apk/repositories \
  && apk update \
  && apk add --no-cache pigz=2.8-r1

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
