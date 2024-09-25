db = db.getSiblingDB('WebApi'); // Cambia al nombre de tu base de datos

// Importar datos desde el archivo JSON
db.User.insertMany(
    JSON.parse(cat('/datos.json'))
);
