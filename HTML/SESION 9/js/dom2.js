const area = document.getElementById("area");
const text2= document.getElementById("text2");

function ocultarTexto() {
    text2.style.display = 'none';
}
function mostrarTexto() {
    text2.style.display = 'block';

}
area.onmouseout = ocultarTexto;
area.onmouseover= mostrarTexto;