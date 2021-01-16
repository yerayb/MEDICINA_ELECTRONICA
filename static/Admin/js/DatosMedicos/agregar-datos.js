function consulta_ajax(medico) {
    var jsonMedico = JSON.stringify(medico);
    console.log(jsonMedico);
    $.ajax({
        url: "/medico",
        type: "POST",
        data: jsonMedico,
        crossDomain: true,
        contentType: "application/json",
        dataType: "json",
        success: function (response) {
            alert("Medico agregado correctamente");
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
    var centroMedico = document.getElementById("centroMedico").value;
    var anyoNacimiento = document.getElementById('anyoNacimiento').value;
    var anyoContratacion = document.getElementById('anyoContratacion').value;
    var salario = document.getElementById('salario').value;
    var especialidad = document.getElementById('especialidad').value;

    var medico = new Object();
    medico.dni = dni;
    medico.nombre = nombre;
    medico.primerApellido = primerApellido;
    medico.segundoApellido = segundoApellido;
    medico.centroMedico = centroMedico;
    medico.anyoNacimiento = anyoNacimiento;
    medico.anyoContratacion = anyoContratacion;
    medico.salario = salario;
    medico.especialidad = especialidad;

    consulta_ajax(medico);

}

