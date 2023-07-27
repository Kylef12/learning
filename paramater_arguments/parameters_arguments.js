
//Parameters
function favGame(game) {  //game is considered to be a parameter as it defines the function.
    console.log(`My fav game is ${game}`)
}
favGame("Madden");
favGame("NCAA");
favGame("COD");  //value inside the fucntion definition are known as arguments

//Multiple Parameters
function racers(kin, car) {
console.log(`${kin} drives a ${car}`);
}
racers("Kyle Busch", "Chevy"); //First argument gets assigned to first parameter and second to the second parameter.
racers("Ryan Blaney", "Ford");  //ex. Kyle Busch = Kin, Chevy = car
racers("Martin Truex Jr.", "Toyota");
racers(); //Empty response will result in undefined message.
racers("Kevin Harvick"); //If only one argument, the argument not given will be undefined.
// If there are more arguments than parameters the function will take the amount that there are parameters and ignore the extra arguments.
//The "Arguments" keyword can be used to index the arguments if there are more than parameters.
//THe "Arguments" keyword would go into the console.log(____) space.

//Default Parameters
function favSport(sport = 'No sport provided') {
    console.log(`My favorite sport is ${sport}`);
}     //A way to have a default value if no input is provided.
favSport();

//Without input
function favSport2(sport) {
   if  (sport === undefined) {
    console.log('Please provide your favorite sport');
   } else {
    console.log(`My favorite sport is ${sport}`);
   }
}     //Default value is required to be added at the end of the list or function call wont work properly.
favSport2();

//With Input
function favSport3(sport) {
    if  (sport === undefined) {
     console.log('Please provide your favorite sport');
    } else {
     console.log(`My favorite sport is ${sport}`);
    }
 }     //Default value is required to be added at the end of the list or function call wont work properly.
 favSport3("Football");