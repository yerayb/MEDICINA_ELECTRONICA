function consulta_ajax(){
    let user = document.getElementById("userLogin").value;
    let pass = document.getElementById("pass").value;

    $.ajax({
        url:"/user?user="+user +"&contraseña=" +pass,
        type: "GET",
        contentType: "application/json",
        success: function(response){
            if(response['usuarioValido'] && response['tipoUsuario'] === 0){
                window.open('../Admin/index.html', '_self');
            }

            if(response['usuarioValido'] && response['tipoUsuario'] === 1){
                window.location.href = '/WebMedico/configPass.html#'+response['usuario'];
            }

            if(response['usuarioValido'] && response['tipoUsuario'] === 2){
                window.location.href = '/WebMedico/index.html#'+response['usuario'];
            }

            else{
                alert("Usuario y/o contreña incorrectos");
            }

            
        },
        error: function(error){
            //console.log(error);
        },
    });


}




