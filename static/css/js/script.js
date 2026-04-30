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
    const usuario = document.getElementById("reg_user").value;
    const correo = document.getElementById("reg_email").value;
    const password = document.getElementById("reg_pass").value;

    fetch("/registro", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ usuario, correo, password })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);

        if(data.mensaje){
            alert("Registro exitoso");
            mostrarLogin();
        } else {
            alert(data.error);
        }
    })
    .catch(err => console.error("Error:", err));
}

// LOGIN
function login(){
    const usuario = document.getElementById("log_user").value;
    const password = document.getElementById("log_pass").value;

    fetch("/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ usuario, password })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);

        if(data.mensaje){
            document.getElementById("login").classList.add("hidden");
            document.getElementById("formulario").classList.remove("hidden");
        } else {
            alert(data.error);
        }
    })
    .catch(err => console.error("Error:", err));
}

// REINSCRIPCIÓN
function enviar(){
    fetch("/reinscripcion", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ ejemplo: "ok" })
    })
    .then(res => res.json())
    .then(data => alert(data.mensaje))
    .catch(err => console.error("Error:", err));
}
