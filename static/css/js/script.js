// CAMBIAR VISTAS
function mostrarLogin(){
    document.getElementById("registro").classList.add("hidden");
    document.getElementById("login").classList.remove("hidden");
}

function mostrarRegistro(){
    document.getElementById("login").classList.add("hidden");
    document.getElementById("registro").classList.remove("hidden");
}

// REGISTRO
function registrar(){
    fetch("/registro", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            usuario: reg_user.value,
            password: reg_pass.value
        })
    })
    .then(res => res.json())
    .then(data => {
        msg_registro.innerText = data.mensaje || data.error;
        if(data.mensaje) mostrarLogin();
    });
}

// LOGIN
function login(){
    fetch("/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            usuario: log_user.value,
            password: log_pass.value
        })
    })
    .then(res => res.json())
    .then(data => {
        if(data.mensaje){
            cargarSesion();
        } else {
            msg_login.innerText = data.error;
        }
    });
}

// CARGAR SESIÓN
function cargarSesion(){
    fetch("/sesion")
    .then(res => res.json())
    .then(data => {
        if(data.usuario){
            document.getElementById("login").classList.add("hidden");
            document.getElementById("registro").classList.add("hidden");
            document.getElementById("panel").classList.remove("hidden");

            usuario_activo.innerText = "Usuario: " + data.usuario;
        }
    });
}

// LOGOUT
function logout(){
    fetch("/logout")
    .then(() => location.reload());
}

// AUTO LOGIN
window.onload = cargarSesion;
