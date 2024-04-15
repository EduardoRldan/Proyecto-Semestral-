console.log ('Hola Mundo');
let nombre = document.getElementById('nombre');
let btnEnviar = document.getElementById('btnEnviar');
btnEnviar.addEventListener("click", function(e){
    e.preventDefault();
    console.log("Esta ingresanado Bien")
})