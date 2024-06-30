const express = require('express');
const app = express();
const port = 3000;

app.use(express());

let videojuegos = [
    {id: 1, nombre: 'Call of Duty 2', Genero:'Shooter en Primera Persona', Plataforma:'PC, XBOX y PLAYSTATION'},
    {id: 2, nombre: 'Assasins Creed', Genero:'Mundo Abierto, 3ra Persona, Sigilo', Plataforma:'PC, XBOX y PLAYSTATION'},
    {id: 3, nombre: 'Need for Spedd Most Wanted', Genero:'Conduccion, Carreras Clandestinas', Plataforma:'PC, XBOX y PLAYSTATION 2'}
];

app.get('/videojuegos',(req, res)=>{
    res.json(Videojuegos);
});

app.get('/videojuegos/:id', (req, res)=>{
    const id = parseInt(req.params.id);
    const Videojuego = Videojuego.find (v => v.id === id);
    if (videojuego) {
        res.json(videojuego);
    }else{
        res.status(404).send('Videojuego no Encontrado');
    }
});

app.post('/Videojuegos', (req, res)=> {
    const nuevoVideojuego = {
        id: videojuegos.length +1,
        nombre: req.body.nombre,
        genero: req.body.genero,
        plataforma: req.body.plataforma,
    };
    videojuegos.push(nuevoVideojuego);
    res.status(201).json(nuevoVideojuego);
});

app.put('/videojuegos/:id',(req, res)=> {
    const id = parseInt(req.param.id);
    const Videojuego = Videojuegos.find(v => v.id === id);
    if (videojuego){
        videojuego.nombre = req.body.nombre;
        Videojuego.genero = req.body.genero;
        videojuego.plataforma = req.body.Plataforma;
        res.json(Videojuego);
    }else{
        res.status(404).send('Videojuego no encontrado');
    }
});

app.delete('/videojuegos/:id',(req, res)=> {
    const id = parseInt(req.params.id);
    const index = videojuegos.findIndex(v => v.id === id);
    if (index !==-1) {
        videojuegos.splice(index, 1);
        res.status(204).send();
    }else{
        res.status(404).send('Videojuego no Encontrado');
    }
});

app.listen(port, () => {
    console.log(`Servidor escuchando en http://localhost:${port}`);
})