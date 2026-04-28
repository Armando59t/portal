function mostrarLogin(){
    registro.classList.add("hidden");
    login.classList.remove("hidden");
}

function mostrarRegistro(){
    login.classList.add("hidden");
    registro.classList.remove("hidden");
}

function registrar(){
    fetch("/registro", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            usuario: reg_user.value,
            correo: reg_email.value,
            password: reg_pass.value
        })
    })
    .then(res => res.json())
    .then(data => alert(data.mensaje || data.error));
}

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
            login.classList.add("hidden");
            formulario.classList.remove("hidden");
        } else {
            alert(data.error);
        }
    });
}

function enviar(){
    fetch("/reinscripcion", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ejemplo: "ok"})
    })
    .then(res => res.json())
    .then(data => alert(data.mensaje));
}
