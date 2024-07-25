class Person{
    //Constructor
    constructor(name, age){
        this.name = name;
        this.age = age;
    }
    //Method
    showInfo(){
        console.log('Name: ' + this.name);
        console.log('Age: ' + this.age);
    }
}
let person1 = new Person('William', 33);
person1.showInfo();
let person2 = new Person('Deniss', 15);
person2.showInfo();