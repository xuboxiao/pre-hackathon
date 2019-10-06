# start postgresql docker containter
docker run --rm --name pg-docker -e POSTGRES_PASSWORD=root -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres

# goes inside postgresql container to run commands
docker exec -tiu postgres pg-docker psql

# list databases
\l

#list tables
\dt

# generate requirements.txt python file
pip freeze > requirements.txt

# build flask docker image
docker build -t hello_world_flask .

# run flask docker container at localhost:8081
docker run --name hello_world -d -p 8081:8080 hello_world_flask
