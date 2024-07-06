//funcion para el inicio de sesion

function login(){
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    if (username && password) {
        const users = JSON.parse(localStorage,getItem('user')) || [];
        const user = user.find(user => user.username === username && user.password === password);

        if (user) {
            alert ('Logeo Iniciado Correctamente');
        }else{
            alert('Usuario o Contraseña Invalida');
        }
    }else{
        alert('Porfavor pinche en las casillas');
    }
}