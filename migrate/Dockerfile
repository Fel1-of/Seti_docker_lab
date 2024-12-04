FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    wget \
    pigz \
    curl  \
    pgloader && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

# Делаем скрипт исполняемым
RUN chmod +x /app/scripts/buildDatabase.sh

# Указываем, что запускать по умолчанию
CMD ["/app/scripts/buildDatabase.sh"]