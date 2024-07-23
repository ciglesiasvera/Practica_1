const students = [
    {name: 'John', grade: 75},
    {name: 'Jane', grade: 93},
    {name: 'Samantha', grade: 90},
    {name: 'Michael', grade: 94}
];
//1. Ordenar en orden descendente
students.sort((a,b ) => b.grade - a.grade);
console.log('Orden descendente:', students);
//2. Reversar el arreglo
students.reverse();
console.log('Reversar el arreglo:', students);
//3. Encontrar el primer estudiante con calificaciones mayoresa 90
const firstStudentAbove90 = students.find(student=>student.grade>90);
console.log('Primer estudiante con calificacion mayor a 90:', firstStudentAbove90);