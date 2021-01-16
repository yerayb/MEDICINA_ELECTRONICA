var options = {
    Alergologia : ["Cetirizina","Desloratadina","Fexofenadina", "Levocetirizina","Loratadina","Difenhidramina","Clorfeniramina"],
    Anestesiologia : ["Anestesia General","Anestesia regional","Control pos anestesico","Epidural", "Sedacion"],
    Angiologia:  ["Ablacion termica","Escleroterapia"],
    Cardiologia: ["Holter implantable", "Ablacion con catéter","Ecocardiografia","IRM Cardiaco"],
    Endocrinologia: ["Glipizida","Linagliptina","Gliburida","Rosiglitazona"],
    Epidemiologia: ["Vacuna Pfizer SARS-COV2", "Vacuna Moderna SARS-COV2", "Vacuna Oxford-Astrazeneca SARS-COV2", "PCR", "Prueba de antigenos", "Analisis de anticuerpos"],
    Oftalmologia: ["Vispring", "Optiben", "Ojosbel", "Visaid Blefresh"]
}

$(function(){
var fillSecondary = function(){
    var selected = $('#primary').val();
    $('#secondary').empty();
    options[selected].forEach(function(element,index){
        $('#secondary').append('<option value="'+element+'">'+element+'</option>');
    });
}
$('#primary').change(fillSecondary);
fillSecondary();
});



function consulta_ajax(prescripcion) {
    var jsonPrescripcion = JSON.stringify(prescripcion);
    $.ajax({
        url: "/prescripcion",
        type: "POST",
        data: jsonPrescripcion,
        crossDomain: true,
        contentType: "application/json",
        dataType: "json",
        success: function (response) {
            alert("prescripcion agregada correctamente");
            window.open('../index.html', '_self');
        },
        error: function (error) {
            alert(error['responseJSON']['mensaje']);

        },
    });


}

function obtenerDatos() {
    var dniPaciente = document.getElementById('dniPaciente').value;
    var especialidad = document.getElementById('primary').value;
    var prestacion = document.getElementById('secondary').value;
    var cantidad = document.getElementById('Cantidad').value;
    var observaciones = document.getElementById('Observaciones').value;

    var fecha = new Date();
    f = fecha.getDate() + "/" + (fecha.getMonth() +1) + "/" + fecha.getFullYear();

    var mes = fecha.getMonth()+1;
    var fecha_reducida = fecha.getDate()+"-"+mes+"-"+fecha.getFullYear();
    var hora = fecha.getHours() +":" +fecha.getMinutes() +":" +fecha.getSeconds();
    var timeStamp = fecha_reducida + " " + hora;
    var idPrescripcion = "Pr-" +timeStamp;
    
    var prescripcion = new Object();
    prescripcion.idPrescripcion = idPrescripcion;
    prescripcion.dniPaciente = dniPaciente;
    prescripcion.especialidad = especialidad;
    prescripcion.prestacion = prestacion;
    prescripcion.fechaEmision = f;
    prescripcion.cantidad = cantidad;
    prescripcion.observaciones = observaciones;
    consulta_ajax(prescripcion);

}

