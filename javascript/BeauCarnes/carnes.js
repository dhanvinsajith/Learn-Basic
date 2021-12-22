console.log('Hello World!')



//COMMENTS
//inline comments
// var number = 5; //comment
/*multi line comment
wowowowoowowo
multiline comment*/



//VARIABLES
/*
var name = "String"; //var can be used throughout the program
var age = 8;
let nname = "String"; //let can only be used within h scope of declaration
const pi = 3.14; //a variable that cannot change
*/



//DECLARING AND ASSIGNING
/*
var a; //value is null
a = 7;
var b = 17;
*/



//BASIC MATH
/*
var a = 5 + 5;
a = 20 - 10
a = 2 * 5
a = 100/10
a++;
a--;
var d = 0.67;
d *= 0.7;
console.log(d)
console.log(a % 6)
a += 5
*/



//STRINGS
/*
var myName = "Dhanvin"
myName = "my name is \"Dhanvin\""
myName += " Sajith."
myName = 'My name is "Dhanvin Sajith".'
console.log(myName)

// \n new line
// \' single quote
// \" double quote
// \\ backslash
// \r carriage return
// \t tab
// \b backspace
// \f form feed

stringLength = myName.length;
firstChar = myName[0];
tenthChar = myName[9]
lastChar = myName[myName.length - 1]
//strings are immutable
*/



//ARRAYS
/*
var mArray = ["Tom", 24, "John, 46"];
mArray = [["Tom", 24], ["John", 46], ["Margaret", 72]];
console.log(mArray[1][0]); //prints 'John'
mArray[2][1] = 73;
mArray.push(["Fred", 35]);
mArray.push("Grenda"); //appends to end
mArray.unshift("Peter") //adds to beginning
end = mArray.pop(); //removes an element from end, end = "Grenda"
first = mArray.shift(); // removes element from front, first = "Peter"
console.log(mArray);
*/  



//FUNCTIONS
/*
function helloWorld(){
    console.log("Hello World!");
}
helloWorld();

function text(word){
    log = word //creating variable thats accessible outside of scope of declaration
    console.log(word); //the variable 'word' is only visible inside scope of function
}
text("Dont do Drugs");
text("Drugs are bad");
console.log("Word was: " + log)

function add(num1, num2){
    console.log(num1 + num2);
}
add(10, 5);

function subtract(num1, num2){
    return num1 - num2;
}
console.log(subtract(10, 5));
subtracted = subtract(10, 5);
console.log(subtracted);

//queueing and for loops
function nextInLine(arr, item){
    for(i in item){
        arr.push(item[i]);
        arr.shift();
    }
    return arr;
}
var mainArr = [1, 2 ,3, 4, 5];
console.log(nextInLine(mainArr, [6, 7, 8, 9, 0]));

//booleans and if, else, else if statements, comparison operators
function greater(num1, num2){
    if num1 === num2{
        return undefined;
    }
    return num1 > num2;
}
if(greater(5, 10) == true){
    console.log("It is greater");
}else if(greater(5, 10) == false){
    console.log("It is lesser");
}

function checkIfTrue(truth){
    if(truth){
        return "It was True."
    }
return "It was False."
}
reality = false
console.log(checkIfTrue(reality))

//equality operators
function checkEqual(one, two){
    if(one == two){ // '==' will try to convert to common datatype before conversion so 10 equals '10'
        console.log("it is equal")
    }else{
        console.log("it is not equal")
    }
}
checkEqual(10, '10')

function checkStrictlyEqual(one, two){
    if(one === two){ // '===' checks if both values and data types are the same
        console.log("they are strictly equal")
    }else{
        console.log("they are not strictly equal")
    }
}
checkStrictlyEqual(10, '10')
checkStrictlyEqual(10, 10)

//inequality works the same way
function checkInequal(one, two){
    if(one != two){
        console.log("it is inequal")
    }else{
        console.log("it is equal")
    }
}
checkInequal(10, '10')

function checkStrictlyInequal(one, two){
    if(one !== two){
        console.log("it is inequal")
    }else{
        console.log("it is equal")
    }
}
checkStrictlyInequal(10, '10')
checkStrictlyInequal('10', '10')
*/



//AND OR OPERATORS
/*
function rollerCoasterCheck(height, age){
    if(height >= 140 && age >= 13 && age < 60){
        console.log("Allowed on the roller coaster.")
    }else{
        console.log("Not allowed on the roller coaster.")
    }
}
rollerCoasterCheck(180, 11)
rollerCoasterCheck(175, 16)
rollerCoasterCheck(120, 18)

function umbreallaRequired(isRaining, isTooHot){
    if(isRaining == true || isTooHot == true){
        console.log("Is required.")
    }else{
        console.log("not required.")
    }
}
umbreallaRequired(false, true)
*/



//SWITCH STATEMENTS
/*
function caseSwitch(val){
    var answer = ""
    switch(val){
        case 1:
            answer = "you typed 1";
            break;
        case 0:
            answer = "you typed zero";
            break;
        case 2:
            answer = "you typed two";
            break;
        case 3:
            answer = "you typed 3";
            break;
        case 4:
        case 5:
        case 6:
            answer = "either 4, 5 or 6";
            break;
        default:
            answer = "value not between 0 and 3";
    }
    return answer;
}
console.log(caseSwitch(5));
*/



//OBJECTS
/*
var dog = {
    "name": "Jonathan",
    "age": 12,
    "healthy": true,
    "friends": ["everything"],
    "likes": ["shoes"]
};
console.log(dog.name + " is " + dog.age + " years old.");
console.log(dog["name"] + " is " + dog["age"] + " years old and likes " + dog["likes"]); //only do this if property name has a space in it
var ageOut = dog["age"]; //now ageOut equals the age of the dog
dog.age = 13; //change property
dog.bark = "ba a r k!! !"; // adding properties
dog["mental stability"] = "insane.";
dog.temp = "temp";
delete dog.temp; //deleting a property off object

var lookup = {
    "alpha": "Adams",
    "bravo": "Boston",
    "charlie": "Chicago"
};
function inLookup(val){
    return lookup[val];
}
console.log(inLookup("bravo")) //look up a value

function checkProperty(property){
    if(lookup.hasOwnProperty(property)){
        return lookup[property];
    }else{
        return "That property does not exist.";
    }
}
console.log(checkProperty("charlie")); //checking for property
console.log(checkProperty("hash browns"));

var matrix = {
    "val1": 2,
    "val2": 3,
    "in1": {
        "valin1": 4,
        "valin2": 5
    },
    "val3": 6,
    "val4": 7
};
console.log(matrix.in1.valin2); //accesing object inside object

//array with two objects
var album = [
    {
        "name": "Sketch",
        "artist": "Scattle",
        "release": 2017,
        "number of songs": 10,
        "best two": ["RGB", "Set In Stone"]
    },
    {
        "name": "Once in a Long, Long While...",
        "artist": "Low Roar",
        "release": 2017,
        "number of songs": 12,
        "best two": ["Don't Be So Serious", "Bones"]
    }
];
var firstAlbumSecondSong = album[0]["best two"][1]; // accessing item in aray in object in array
console.log(firstAlbumSecondSong);
*/



//LOOPS
/*
//while loop
var array = []
var i  = 0
while(i < 5){
    i += 1
    array.push(i);
}
console.log(array);

//for loop
for(var j = 6; j <= 10; j++){
    array.push(j);
}
console.log(array)

oddArr = []
for(var j = 1; j < 10; j += 2){
    oddArr.push(j);
}
console.log(oddArr);

backArr = [];
for(var i = 9; i > 0; i -= 2){
    backArr.push(i);
}
console.log(backArr);

var oddSum = 0;
for(var i = 0; i < oddArr.length; i++){
    oddSum += oddArr[i];
}
console.log(oddSum);

//nested loops
for(var i = 1; i < 6; i++){
    var output = "";
    for(var j = 1; j < i+1; j++){
        output += "*";
    }
    console.log(output);
}

//do.. while loops
var i = 10;
do{
    console.log("do while loop always executes atleast once");
}while(i < 0)
*/



//USEFUL FUNCTIONS
/*
//random fraction between 0 and 1
function randomFrac(){
    return "Random fraction: " + Math.random();
}
console.log(randomFrac());

//random whole number from 0 to 19
function randomWhole(){
    return "Random whole number: " + Math.floor(Math.random() * 20);
}
console.log(randomWhole());

//random in range
function randRange(min, max){
    return "Random in range: " + (Math.floor(Math.random() * (max - min + 1)) + min);
}
console.log(randRange(50, 60));

//convert string to integer
function convertToInt(str){
    return parseInt(str) || "cannot be converted";
}
console.log(convertToInt('57'));
console.log(convertToInt('test'));

//convert to different number system
function convertFromBinary(str){
    return parseInt(str, 2);
}
console.log(convertFromBinary('1010'))

//ternary operation(one line if else statement)
function ternaryTest(a, b){
    a === b ? console.log("Equal") : console.log("Not Equal");
}
ternaryTest(5, 6);
ternaryTest(5, 5);
ternaryTest(5, '5');

//nested ternaries
function checkSign(num){
    return num > 0 ? "positive" : num < 0 ? "negative" : "zero";
}
console.log(checkSign(-5));
console.log(checkSign(5));
console.log(checkSign(0));
*/



//VAR, LET, CONST
/*
//wont raise error
var num = 0;
var num = 9;

//will raise error
// let sum = 0;
// let sum = 0;

//lat variables cant be declared more than once
//scope of let is only in scope of declaration

//will raise error because const is read only cannot be reassigned, constants are all caps
// const COOL = "I am cool";
// COOL = "He is cool";

//arrays declared with const can be modified
const arr = [1, 3, 5];
arr[1] = 9;;
console.log(arr);

//prevents mutation of const object
const array = [2, 4, 6];
Object.freeze(array);
console.log(array);
*/



//ARROW FUNCTIONS
/*
var magic_ = function(){
    return new Date();
};
//is the same as
const magic = () => new Date();

//parameters
var concatenate_ = function(arr1, arr2){
    return arr1.concat(arr2);
};
console.log(concatenate_([1, 2], [3, 4]));

//default parameter
var concatenate = (array1, array2 = [1, 2]) => array1.concat(array2);
console.log(concatenate([3, 4]));

//rest operator (dots)
const sum = (...args) => console.log(args.reduce((a, b) => a + b, 0));
sum(1, 2, 3, 4);

//spread operator (analyze content)
const MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun'];
let content;
(function(){
    content = [...MONTHS];
    MONTHS[2] = 'oct';
})();
console.log(MONTHS);
console.log(content);
*/



//DESTRUCTURING
/*
var object = {x: 6.7, y: 8.2, z: 2.1};

var x = object.x;
var y = object.y;
var z = object.z;
//is same as
const{x:a, y:b, z:c} = object;
console.log(a, b, c)

//nested objects
const FORECAST = {
    today:{min: 21, max:31},
    tomorrow:{min:19, max:26}
};
const {tomorrow : {max : tom_max}} = FORECAST;
console.log(tom_max);

//from arrays
const [friends, , , , , , , pi] = [0, 0.14, 1, 1.14, 2, 2.14, 3, 3.14, 4, 4.14];
console.log(friends)
console.log(pi)

//reassigning opposite
let n = 7;
let m = 8;
console.log(n, m);
[n, m] = [m, n]
console.log(n, m);

//destructuring with rest
ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const [ , , ...arr] = ten;
console.log(ten)
console.log(arr)

//passing object into function
const STATS = {
    min: -0.75,
    max: 56.78,
    mean: 35.85,
    median: 34.54,
    mode: 23.87,
    standard_deviation: 4.34
};
const half = (function(){
    return function half({max, min}){ //pass in what you need
        return (max + min) / 2.0;
    };
})();
console.log(STATS);
console.log(half(STATS));
*/



//TEMPLATE LITERAL (fstring)
/*
const person = {
    name: "F String",
    age: 25
};

const comp = {
    name: 'Template Literal'
}

const greeting = `Hello ${person.name}!
I am ${comp.name}. You are ${person.age} years old.` //easy variable adding and multiline formatting

console.log(greeting)
*/



//CLASSES
/*
// var spaceShuttle = function(planet){
//     this.planet = planet;
// }
// var artemis = new spaceShuttle('Saturn');

// console.log(artemis.planet);

//can be done as

class spaceShuttle{
    constructor(planet){
        this.planet = planet;
    }

    //getters
    get destination(){
        return this.planet;
    }

    //setters
    set destination(updatedPlanet){
        this.planet = updatedPlanet;
    }
}
var artemis = new spaceShuttle('Saturn');
console.log(artemis.planet);

//getters and setters
ogPlanet = artemis.destination;
artemis.destination = 'Neptune';
console.log(artemis.planet);
console.log(ogPlanet)
*/



//IMPORT AND EXPORT
//exporting a function from one file makes it accessible by using import in another file
//use * to import everything from a file