docker run --rm --name pg-docker -e POSTGRES_PASSWORD=root -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres
docker exec -tiu postgres pg-docker psql
\l
\dt

