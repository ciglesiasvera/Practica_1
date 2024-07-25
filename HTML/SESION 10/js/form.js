$(document).ready(function(){
    //método para escuchar el evento tipo submit del formulario
    $('#simpleForm').on('submit',function(event){
        //Evita el reenvío de formulario
        event.preventDefault();
        let isValid = true;
        let errorMessage = "";
        let successMessage = "";
    //eliminar mensajes previos
    $('.error').remove();
    $('#formMessage').empty();
    //Form validation
    const username = $('#username').val().trim();
        if (username === "") {
            isValid=false;
            $('#username').after('<span class="error">El nombre de usuario es obligatorio</span>');
        }
        const email = $('#email').val().trim();
        if (email === '') {
            isValid = false;
            $('#email').after('<span class="error">El correo electrónico es obligatorio.</span>');
        } else {
            const emailPattern = /^[^@]+@[^@]+\.[a-zA-Z]{2,}$/;
            if (!emailPattern.test(email)) {
                isValid = false;
                $('#email').after('<span class="error">Ingrese un correo electrónico válido.</span>');
            }
        }    
        //Password validation
        const password = $('#password').val().trim();
        if(password === ""){
            isValid=false;
            $('#password').after('<span class="error">La contraseña es obligatoria</span>');
        }
        if(isValid){
            successMessage='<p class="success">Formulario enviado exitosamente</p>'
            $('#formMessage').html(successMessage);
        //Aquí se manipula para enviar el formulario
        }else{
            errorMessage = '<p class="error>Por favor corriege los errores</p>';
            $('#formMessage').html(errorMessage);
        }
    });
});