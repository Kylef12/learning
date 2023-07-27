//Basic function
function games(){
    alert('Super Mario');
    alert('Madden');
}
games()  //calls the function, a function can be called multiple times
alert(games)  //shows function code rather than run the function

//Function with local variable(s)
function games2(){
    let title = "NCAA" //local variable
    alert(title);
}
games2() //calls the function

//Function with local and global variable(s)
let greeting = "hey, world"; //global variable
function games3(){
    let title ="Zelda" //local variable
    alert(title,greeting);
}
games3();
alert(greeting);

//Function with no declared name
let btn = document.querySelector('#btn');
btn.addEventListener('click',function() {
    alert("You clicked");
});


