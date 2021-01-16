
function cargarDatos(response){
    var medicosJson = JSON.parse(JSON.stringify(response));

    for (i = 0; i < medicosJson.length; i++){

        $("#dataTable").append('<tr>' +
            '<td align="left" style="dislay: none;">' + medicosJson[i]['dni'] + '</td>'+
            '<td align="left" style="dislay: none;">' + medicosJson[i]['nombre'] + " " + medicosJson[i]['primerApellido'] + " " + medicosJson[i]['segundoApellido'] + '</td>'+
            '<td align="left" style="dislay: none;">' + medicosJson[i]['nombre'].substring(0,2).toLowerCase() + medicosJson[i]['primerApellido'].substring(0,2).toLowerCase() + medicosJson[i]['segundoApellido'].substring(0,2).toLowerCase()  + '</td>'+
            '<td align="left" style="dislay: none;">' + medicosJson[i]['especialidad'] + '</td>'+
            '<td align="left" style="dislay: none;">' + medicosJson[i]['centroMedico'] + '</td>'+
            '<td align="left" style="dislay: none;">' + medicosJson[i]['anyoNacimiento'] + '</td>'+
            '<td align="left" style="dislay: none;">' + medicosJson[i]['anyoContratacion'] + '</td>'+
            '<td align="left" style="dislay: none;">' + medicosJson[i]['salario'] + '</td>' +'</tr>');
    }
}

function consulta_ajax() {
    $.ajax({
        url: "/medicos",
        type: "GET",
        contentType: "application/json",
        success: function (response) {
            console.log(response);
            cargarDatos(response);
        },
        error: function (error) {
            alert("Error al intentar registrar un nuevo medico");
        },
    });


}

window.onload = consulta_ajax();

