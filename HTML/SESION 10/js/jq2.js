$(document).ready(function(){
    //método para ocultar y mostrar un texto
    $('#toggleButton').click(function(){
        $('#paragraph2').toggle();
    })
    //método para cambiar el colo de fondo con un evento de mouse
    $('#paragraph3').mouseenter(function(){
        $(this).css("background-color","yellow");
    }).mouseleave(function(){
        $(this).css("background-color","white");
    })
    //animar una caja
    $(animatedButton).click(function(){
    $('#box').animate({
        width:"200px",
        height:"200px",
    }, 1000);
    })
});