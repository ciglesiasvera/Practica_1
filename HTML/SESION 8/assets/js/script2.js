// Estructura de datos
const alumnos = [
    { nombre: "Roberto Hernandez", calificaciones: [6, 5, 7] },
    { nombre: "Maria Perez", calificaciones: [3, 2, 1] },
    { nombre: "Juan Lopez", calificaciones: [7, 6, 5] }
];

// Función para ver la lista de alumnos
function verListaDeAlumnos() {
    console.log("Lista de Alumnos:");
    alumnos.forEach((alumno, index) => {
        console.log(`${index + 1}. Nombre: ${alumno.nombre}`);
    });
}

// Función para ver calificaciones de los alumnos
function verCalificaciones() {
    alumnos.forEach((alumno, index) => {
        console.log(`Calificaciones de ${alumno.nombre}:`);
        alumno.calificaciones.forEach((calificacion, idx) => {
            const estado = calificacion >= 4 ? 'Aprobado' : 'Reprobado';
            console.log(`  Calificación ${idx + 1}: ${calificacion}, ${estado}`);
        });
    });
}

// Función para calcular el promedio del grupo
function calcularPromedio() {
    let sumaTotal = 0;
    let cantidadCalificaciones = 0;

    alumnos.forEach(alumno => {
        alumno.calificaciones.forEach(calificacion => {
            sumaTotal += calificacion;
            cantidadCalificaciones++;
        });
    });

    const promedio = sumaTotal / cantidadCalificaciones;
    console.log(`El promedio del grupo es: ${promedio.toFixed(1)}`);
}

// Menú del sistema
function mostrarMenu() {
    console.log("Menú del Sistema:");
    console.log("1. Ver lista de alumnos");
    console.log("2. Ver calificaciones de alumnos");
    console.log("3. Calcular el promedio del grupo");
    console.log("4. Salir");
}

// Función para manejar las opciones del menú
function manejarMenu(opcion) {
    switch(opcion) {
        case 1:
            verListaDeAlumnos();
            break;
        case 2:
            verCalificaciones();
            break;
        case 3:
            calcularPromedio();
            break;
        case 4:
            console.log("Saliendo del sistema...");
            return;
        default:
            console.log("Opción no válida. Por favor, elija una opción del 1 al 4.");
    }
    // Mostrar el menú de nuevo después de ejecutar una opción
    mostrarMenu();
}

// Mostrar el menú al inicio
mostrarMenu();

// Simulación de la elección del usuario
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.on('line', (input) => {
    const opcion = parseInt(input.trim(), 10);
    if (opcion === 4) {
        readline.close();
    }
    manejarMenu(opcion);
});