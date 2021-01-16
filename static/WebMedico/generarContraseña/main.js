function generarContraseña(){
    var usuario = window.location.hash.substring(1);
    var contraseña = document.getElementById('passGenerator').value;

    var userDB = new Object();
    userDB.usuario = usuario;
    userDB.contraseña = contraseña;

    var jsonUsuario = JSON.stringify(userDB);

    $.ajax({
        url: "/user/" + usuario,
        type: "POST",
        contentType: "application/json",
        data: jsonUsuario,
        dataType: "json",
        success: function (response) {
            console.log("Exito");
            window.location.href = '/';

        },
        error: function (error) {
            //console.log(error);
        },
    });
    


}