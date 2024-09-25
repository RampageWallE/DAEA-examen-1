const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const axios = require("axios");
const mongoose = require("mongoose");
const User = require("./models/User");

const app = express();

app.use(bodyParser.json()); // Para analizar cuerpos JSON
app.use(bodyParser.urlencoded({ extended: true })); 
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));


const API_URL = "http://api:8080";

const port = 3000;

app.get('/', async (req, res) => {
    try{
        const response = await axios.get(`${API_URL}/api/user/all2`);
        const usuario = response.data;
        console.log(usuario);
        res.render('user2', usuario)
    }catch(error){
        res.json(error)
    }
})


app.get('/search', async (req, res) => {
    const query = req.query.query;

    try {
        // Realizar la solicitud a la API de Python
        const response = await axios.get(`http://apisearch:5000/search?query=${query}`);
        
        // Devolver los resultados a quien realizó la solicitud
        res.status(200).render('user', {results : response.data});
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Error al buscar usuarios en la API de Python' });
    }
});

app.get('/users', async (req, res) => {
    try{
        const users = await axios.get(`${API_URL}/api/user/all`);
        // const users = await User.find();
        res.status(200).render('user', {results : users.data})

    }catch(err){
        res.status(500).send({message: "Error al obtener usuarios", error: err})
    }
})


app.listen(port, () => {
    console.log("EL servidor esta siendo ejecutado en el puerto http://localhost:3000")
} )