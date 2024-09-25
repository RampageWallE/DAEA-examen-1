# Usar la imagen oficial de MongoDB como base
FROM mongo:latest

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo JSON al contenedor
COPY ./WebApi.User.json /datos.json

# Importar datos al iniciar el contenedor
CMD ["mongosh", "--eval", "db = db.getSiblingDB('WebApi'); db.User.drop(); db.User.insertMany(JSON.parse(cat('/datos.json')));"]

