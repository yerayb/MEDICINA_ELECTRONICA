function consulta_ajax() {

    $("#userInfo").empty();

    //dni introducido
    let dni = document.getElementById("dni").value;

    $.ajax({
        url: "/medico/" + dni,
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
    $("#userInfo").append('<br>' +"Especialidad: " +response['especialidad']);
    // Get the button that opens the modal
    var btnConfirmar = document.getElementById("btnConfirmar");

    // Get the button that opens the modal
    var btnCancelar = document.getElementById("btnCancelar");

    btnCancelar.onclick = function(){
        modal.style.display = "none";
    };

    btnConfirmar.onclick = function(){
        $.ajax({
            url: "/medico/" + dni,
            type: "DELETE",
            contentType: "application/json",
            success: function (response) {
            },
            error: function (error) {
                //console.log(error);
            },
        })

        $.ajax({
            url: "/user/" + dni,
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