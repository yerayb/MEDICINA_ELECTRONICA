function consulta_ajax() {

    //dni introducido
    let dni = document.getElementById("dni").value;

    $("#userInfo").empty();


    $.ajax({
        url: "/paciente/" + dni,
        type: "GET",
        contentType: "application/json",
        success: function (response) {
            verModalModificar(response);
        },
        error: function (error) {
            //console.log(error);
        },
    })

}

function verModalModificar(response) {
    //dni introducido
    let dni = document.getElementById("dni").value;

    //Añadir info Usuario al modal
    $("#userInfo").append("DNI: " +dni);

    // Get the modal
    var modal = document.getElementById("myModal");
    modal.style.display = "block";

    $("#userInfo").append('<br>' +"Nombre: " +response['nombre']);
    // Get the button that opens the modal
    var btnConfirmar = document.getElementById("btnConfirmar");

    // Get the button that opens the modal
    var btnCancelar = document.getElementById("btnCancelar");

    btnCancelar.onclick = function(){
        modal.style.display = "none";
    };

    btnConfirmar.onclick = function(){
        $.ajax({
            url: "/paciente/" + dni,
            type: "DELETE",
            contentType: "application/json",
            success: function (response) {
            },
            error: function (error) {
                //console.log(error);
            },
        })

    };


// When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

}