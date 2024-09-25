#!/bin/sh

git clone https://github.com/RampageWallE/DAEA-examen-1.git app

cd app 

docker compose up -d --build 

# Duerme un momento
sleep 3

# Cambiar al directorio db
cd db || { echo "Directorio 'db' no encontrado."; exit 1; }

# Copiar el archivo JSON al contenedor
docker cp WebApi.User.json db:/data/WebApi.User.json

# Ejecutar mongoimport dentro del contenedor
docker exec -it db /bin/sh -c "mongoimport --db WebApi --collection User --file /data/WebApi.User.json --jsonArray --username root --password example --authenticationDatabase admin"
