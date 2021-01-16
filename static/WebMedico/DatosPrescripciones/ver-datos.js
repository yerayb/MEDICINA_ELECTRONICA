
function cargarDatos(response){
    var prescripcionesJson = JSON.parse(JSON.stringify(response));

    for (i = 0; i < prescripcionesJson.length; i++){

        $("#dataTable").append('<tr>' +
            '<td align="left" style="dislay: none;">' + prescripcionesJson[i]['idPrescripcion'] + '</td>'+
            '<td align="left" style="dislay: none;">' + prescripcionesJson[i]['dniPaciente'] + '</td>'+
            '<td align="left" style="dislay: none;">' + prescripcionesJson[i]['Paciente'] + '</td>'+
            '<td align="left" style="dislay: none;">' + prescripcionesJson[i]['Especialidad'] + '</td>'+
            '<td align="left" style="dislay: none;">' + prescripcionesJson[i]['Prestacion'] + '</td>'+
            '<td align="left" style="dislay: none;">' + prescripcionesJson[i]['FechaEmision'] + '</td>'+
            '<td align="left" style="dislay: none;">' + prescripcionesJson[i]['Cantidad'] + '</td>'+
            '<td align="left" style="dislay: none;">' + prescripcionesJson[i]['Observaciones'] + '</td>' +'</tr>');
    }
}

function consulta_ajax() {
    $.ajax({
        url: "/prescripciones",
        type: "GET",
        contentType: "application/json",
        success: function (response) {
            console.log(response);
            cargarDatos(response);
        },
        error: function (error) {
           
        },
    });


}

window.onload = consulta_ajax();

