alert("Bienvenidos a la calculadora básica");
console.log("Bienvenidos a la calculadora básica");
alert("Elige una opcion: 1. Suma, 2. Resta, 3. Multiplicacion, 4. Division");
opcion=parseInt(prompt("Escribe el numero de opcion"));
var a;
var b;
a = parseInt(prompt("Ingresa un número"));
b = parseInt(prompt("Ingresa otro número"));
if (a==0 && b ==0) {
    alert("El denominador debe ser distinto de cero");
}
switch(opcion) {
    case 1:
        total = suma(a,b);
        alert("El resultado de la suma es " + total);
        break;
    case 2:
        total1 = resta(a,b);
        alert("El resultado de la resta es " + total1);
        break;
    case 3:
        total2 = multiplicacion(a,b);
        alert("El resultado de la multiplicacion es " + total2);
        break;
    case 4:
        total3 = division(a,b);
        alert("El resultado de la division es " + total3);
        break;
}
alert("Gracias por utilizar esta calculadora")
total=(parseInt(a)+ parseInt(b));
total = suma(a,b);
alert("El resultado de la suma es:" + total);
total1 = resta(a,b);
alert("El resultado de la resta es:" + total1);
total2 = multiplicacion(a,b);
alert("El resultado de la multiplicacion es:" + total2);
total3 = division(a,b);
alert("El resultado de la division es:" + total3);

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
        resultado = a/b;
        return resultado;
    }