FROM python:3.13.0-alpine3.20

WORKDIR app/

RUN echo https://mirrors.dotsrc.org/alpine/v3.20/main > /etc/apk/repositories \
  && echo https://mirrors.dotsrc.org/alpine/v3.20/community >> /etc/apk/repositories \
  && apk update \
  && apk add --no-cache pigz=2.8-r1

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 5000

# ENV FLASK_DEBUG=1
# CMD flask -A sdow/server.py:load_app run --host=0.0.0.0

CMD ["gunicorn", "sdow.server:load_app('prod')", "-c", "config/gunicorn.conf.py"]