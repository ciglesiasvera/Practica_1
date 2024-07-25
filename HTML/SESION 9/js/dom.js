// obtener elementos del dom y guardarlo en variables
const titulo= document.getElementById("titulo");
const descripcion= document.getElementById("descripcion");
const botonAgregar= document.getElementById("botonAgregar");
const botonCambiar= document.getElementById("botonCambiar");

function agregarElemento() {
    //crear un nuevo elemento <p>
     const nuevoParrafo = document.createElement("p");
    //anadir un texto al elemento
     nuevoParrafo.textContent = "Este un nuevo parrafo agregado desde JS";
     // anadir una clase al nuevo al elemento
     nuevoParrafo.classList.add("nuevo-elemento");
     // inserta un elemento en body
     document.body.appendChild(nuevoParrafo);
}
function cambiarValor(){
    // cambia el contenido del parrafo
    descripcion.textContent = "Aqui estuvo Roberto!!!";
    descripcion.classList.add("resaltado");
}

botonAgregar.addEventListener("click", agregarElemento);
botonCambiar.addEventListener("click", cambiarValor);
