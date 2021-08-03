docker run -d --name "osairis-postgres" \
    -u 0:0 \
    -p 5432:5432 \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=postgres \
    -v $(pwd)/postgres-data:/var/lib/postgresql/data \
    --network osairis-bridge \
    osairis-postgres:latest
