var text = window.location.hash.substring(1);
console.log(text);
window.onload = function(){
    $("#dni").val(text);
    consulta_ajax();
}


function consulta_ajax() {
    $.ajax({
        url: "/paciente/" + text,
        type: "GET",
        contentType: "application/json",
        success: function (response) {
            $("#nombre").val(response['nombre']);
            $("#primerApellido").val(response['primerApellido']);
            $("#segundoApellido").val(response['segundoApellido']);
            $("#direccion").val(response['direccion']);
            $("#anyoNacimiento").val(response['anyoNacimiento']);
            $("#cp").val(response['CP']);
            $("#municipio").val(response['municipio']);
            $("#provincia").val(response['provincia']);
            $("#telefono").val(response['telefono']);
            $("#email").val(response['email']);
            $("#sexo").val(response['sexo']);
        },
        error: function (error) {
            //console.log(error);
        },
    });
}

function modificarPaciente() {
    var dni = document.getElementById('dni').value;
    var nombre = document.getElementById('nombre').value;
    var primerApellido = document.getElementById('primerApellido').value;
    var segundoApellido = document.getElementById('segundoApellido').value;
    var direccion = document.getElementById("direccion").value;
    var anyoNacimiento = document.getElementById('anyoNacimiento').value;
    var CP = document.getElementById('cp').value;
    var municipio = document.getElementById('municipio').value;
    var provincia = document.getElementById('provincia').value;
    var telefono = document.getElementById('telefono').value;
    var email = document.getElementById('email').value;
    var sexo = document.getElementById('sexo').value;

    var paciente = new Object();
    paciente.dni = dni;
    paciente.nombre = nombre;
    paciente.primerApellido = primerApellido;
    paciente.segundoApellido = segundoApellido;
    paciente.direccion = direccion;
    paciente.CP = CP;
    paciente.municipio = municipio;
    paciente.provincia = provincia;
    paciente.anyoNacimiento = anyoNacimiento;
    paciente.telefono = telefono;
    paciente.email = email;
    paciente.sexo = sexo;

    var jsonPaciente = JSON.stringify(paciente);

    $.ajax({
        url: "/paciente/" + text,
        type: "POST",
        contentType: "application/json",
        data: jsonPaciente,
        dataType: "json",
        success: function (response) {

        },
        error: function (error) {
            //console.log(error);
        },
    });

    alert("Paciente modificado correctamente");
    window.open('../index.html', '_self');
}