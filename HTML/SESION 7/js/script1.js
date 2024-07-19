alert("Bienvenidos a la calculadora básica");
console.log("Bienvenidos a la calculadora básica");
var a;
var b;
var total;
//a=90331;
a = prompt("Ingresa un número");
//b=90332;
b = prompt("Ingresa otro número");
//total=(parseInt(a)+ parseInt(b));
total = suma(a,b);
alert("El resultado de la suma es:" + total);
total1 = resta(a,b);
alert("El resultado de la resta es:" + total1);
total2 = multiplicacion(a,b);
alert("El resultado de la multiplicacion es:" + total2);
total3 = division(a,b);
alert("El resultado de la division es:" + total3);
if (total3 == 0) {
    alert("Operación Vacía")
}
alert("Gracias por utilizar esta calculadora")

function suma(a,b) {
    resultado = parseInt(a) + parseInt(b);
    return resultado;
}

function resta(a,b) {
    resultado = a - b;
    return resultado;
}

function multiplicacion (a,b) {
    resultado = a * b;
    return resultado;
}

function division (a,b) {
    if(b!=0){
        resultado = a/b;
    }else{
        alert("El denominador debe ser distinto de cero");
    }
}