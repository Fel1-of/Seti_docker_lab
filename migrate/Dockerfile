FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    wget \
    pigz \
    curl  \
    pgloader && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN chmod +x scripts/buildDatabase.sh

CMD ["./scripts/buildDatabase.sh"]