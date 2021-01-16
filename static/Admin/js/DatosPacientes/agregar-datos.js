function consulta_ajax(paciente) {
    var jsonPaciente = JSON.stringify(paciente);
    console.log(jsonPaciente);
    $.ajax({
        url: "/paciente",
        type: "POST",
        data: jsonPaciente,
        crossDomain: true,
        contentType: "application/json",
        dataType: "json",
        success: function (response) {
            alert("Paciente agregado correctamente");
            window.open('../index.html', '_self');
        },
        error: function (error) {
            console.log("Hola");
            alert(error['responseJSON']['mensaje']);

        },
    });


}

function obtenerDatos() {
    var dni = document.getElementById('dni').value;
    var nombre = document.getElementById('nombre').value;
    var primerApellido = document.getElementById('primerApellido').value;
    var segundoApellido = document.getElementById('segundoApellido').value;
    var direccion = document.getElementById("direccion").value;
    var anyoNacimiento = document.getElementById('anyoNacimiento').value;
    var cp = document.getElementById('cp').value;
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
    paciente.cp = cp;
    paciente.municipio = municipio;
    paciente.provincia = provincia;
    paciente.anyoNacimiento = anyoNacimiento;
    paciente.telefono = telefono;
    paciente.email = email;
    paciente.sexo = sexo;

    consulta_ajax(paciente);

}

