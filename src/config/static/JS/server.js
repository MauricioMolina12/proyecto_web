const express = require('express');
const cors = require('cors');
const app = express();
app.use(cors());
app.post('/saveusuario', (req, res) => {
    // Código para guardar el usuario
    res.send('Usuario guardado');
});
app.listen(5000, () => {
    console.log('Servidor escuchando en el puerto 5000');
});