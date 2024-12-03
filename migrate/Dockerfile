FROM postgres:latest

WORKDIR /app

COPY . .

RUN chmod +x scripts/buildDatabase.sh

ENTRYPOINT ["./app/scripts/buildDatabase.sh"]