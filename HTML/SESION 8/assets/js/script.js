/* var num_articulos =parseInt(prompt("Numero de articulos que desea comprar"));
for(var inicio=1; inicio<=num_articulos; inicio++){
    var precio_articulo = parseInt(prompt("Dame precio de artículo" + inicio))
    var cant_articulo = parseInt(prompt("Dame cantidad de artículo" + inicio))
console.log("Precio de articulo "+ precio_articulo);
console.log("Cantidad de articulo "+ cant_articulo);
console.log(calcular_Subtotal(precio_articulo,cant_articulo));
}
//ciclo do while
var numero = parseInt(prompt("Ingresa un numero"));
var x=1
do{
    console.log("x");
    x = x + 1;
}while(x < numero); */
//try catch
var numero2 = parseInt(prompt("Ingresa un numero"));
try{
    if(numero2!=10) throw new Error("El número no es 10");
    console.log("La ejecución se hizo de manera correcta");
}catch (error){
    console.log("error.name, error.message");
}
function calcular_Subtotal(precio_articulo,cant_articulo){
    subtotal = precio_articulo * cant_articulo;
    return subtotal;
}