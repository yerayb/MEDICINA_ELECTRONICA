var text = window.location.hash.substring(1);
console.log(text);
window.onload = function(){
    $("#dni").val(text);
    consulta_ajax();
}


function consulta_ajax() {
    $.ajax({
        url: "/medico/" + text,
        type: "GET",
        contentType: "application/json",
        success: function (response) {
            $("#nombre").val(response['nombre']);
            $("#primerApellido").val(response['primerApellido']);
            $("#segundoApellido").val(response['segundoApellido']);
            $("#centroMedico").val(response['centroMedico']);
            $("#anyoNacimiento").val(response['anyoNacimiento']);
            $("#anyoContratacion").val(response['anyoContratacion']);
            $("#salario").val(response['salario']);
            $("#especialidad").val(response['especialidad']);
        },
        error: function (error) {
            //console.log(error);
        },
    });
}

function modificarMedico() {
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

    var jsonMedico = JSON.stringify(medico);

    $.ajax({
        url: "/medico/" + text,
        type: "POST",
        contentType: "application/json",
        data: jsonMedico,
        dataType: "json",
        success: function (response) {

        },
        error: function (error) {
            //console.log(error);
        },
    });

    alert("Medico modificado correctamente");
    window.open('../index.html', '_self');
}