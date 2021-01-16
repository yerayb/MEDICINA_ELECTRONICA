
function cargarDatos(response){
    var pacientesJson = JSON.parse(JSON.stringify(response));

    for (i = 0; i < pacientesJson.length; i++){

        $("#dataTable").append('<tr>' +
            '<td align="left" style="dislay: none;">' + pacientesJson[i]['dni'] + '</td>'+
            '<td align="left" style="dislay: none;">' + pacientesJson[i]['nombre'] + " " + pacientesJson[i]['primerApellido'] + " " + pacientesJson[i]['segundoApellido'] + '</td>'+
            '<td align="left" style="dislay: none;">' + pacientesJson[i]['anyoNacimiento'] + '</td>'+
            '<td align="left" style="dislay: none;">' + pacientesJson[i]['municipio'] + '</td>'+
            '<td align="left" style="dislay: none;">' + pacientesJson[i]['provincia'] + '</td>'+
            '<td align="left" style="dislay: none;">' + pacientesJson[i]['sexo'] + '</td>'+
            '<td align="left" style="dislay: none;">' + pacientesJson[i]['email'] + '</td>'+
            '<td align="left" style="dislay: none;">' + pacientesJson[i]['telefono'] + '</td>' +'</tr>');
    }
}

function consulta_ajax() {
    $.ajax({
        url: "/pacientes",
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

