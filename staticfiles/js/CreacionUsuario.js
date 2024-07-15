//Script para la creacion de Usuario


//funcion de registro de usuario
function register(){
    const username = document.getElementById('reg-username').value;
    const email = document.getElementById('reg-email').value;
    const password = document.getElementById('reg-password').value;

    if (username && email && password){
        const users = JSON.parse(localStorage,getItem(users)) || [];
        const usersExists = user.some(user => user.username === username || user.email === email);

        if (usersExists){
            alert('Usuario o Email ya existentes');
            return;
        }
        user.push({username, email, password});
        localStorage.setItem('users',JSON.stringify(user));
        alert('Porfavor pinche en las casillas');
    }

}