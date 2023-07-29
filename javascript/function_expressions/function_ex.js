//Function expressions are functions which are created inside an expression or inside another syntax constructor.
//Basically use functions without a name create functions.

//Basic Function Expression
let games = function () { //example of function expression
console.log('Madden');
console.log('NCAA');
console.log('COD');
}

games();   //Function expression doesn't require name but can include one.

//Reassigning a function expression
let games2 = function () { //example of function expression
    console.log('Madden');
    console.log('NCAA');
    console.log('COD');
    }
    
    let newWayToCall = games2; //Reassigning is simply just changing the name and using the new name to call the function.
    newWayToCall();

//Invoking function before declaring

myFunc();

function myFunc() {
    console.log("Calling function");
}     //This works because the function is globally stored and javascript searches for globally stored functions in its memory.

myFunc2();

let myFunc2 = function() {
    console.log("Calling function");
}   //This doesn't work because the function is anonymous.


