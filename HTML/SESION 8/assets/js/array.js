// Declar una arreglo
var  regiones = ["Santiago","Antofagasta", "Viña del Mar","Biobio"];
// imprimir arreglo
console.log(regiones);
//obtiene un posicion especifica de un arreglo
console.log(regiones[2]);


// Recorriendo un arreglo y agregamos una cadena
for (var i = 0; i < regiones.length; i++) { 
    console.log("Nombre de la region es:" + regiones[i]);
}
regiones.push("Maule");
console.log(regiones);
console.log("que pasa..")
regiones.pop();
console.log(regiones);
regiones.shift();
console.log(regiones);
regiones.unshift("Los lagos");

// Recorremos un arreglo y hacemos una operacion
var precios=[802,910,1221,218,346]
for (var i = 0; i < precios.length; i++){
    console.log(precios[i]);
    console.log(precios[i]* 1.19);
}