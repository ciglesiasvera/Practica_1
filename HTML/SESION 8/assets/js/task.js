class Task{
    //Constructor
    constructor(taskName, status){
        this.taskName = taskName;
        this.status = status;
        this.changeStatus = changeStatus;

        /*this.changeStatus = function(){
            console.log("The Task is completed!");
        } */
    }
    //Method
    showTasks(){
        console.log('Task Name: ' + this.taskName);
        console.log('Status: ' + this.status);
    }
    showStatus(){
        console.log('Task Name: ' + this.taskName);
        console.log('Status: ' + this.changeStatus);
    }
}
let task1 = new Task('Origami Crafts', 'Incomplete');
let task2 = new Task('Math Homework', 'Started');
let task3 = new Task('History Homework', 'Incomplete');
let task4 = new Task('Physics Exercises', 'Completed');
task1.showTasks();
task2.showTasks();
task3.showTasks();
task4.showTasks(); 

let task5 = new Task('Origami Crafts', 'Incomplete');
let task6 = new Task('Math Homework', 'Started');
let task7 = new Task('History Homework', 'Incomplete');
let task8 = new Task('Physics Exercises', 'Completed');

task1.changeStatus();
task2.changeStatus();
task3.changeStatus();
task4.changeStatus();