// 1. output
console.log("hello world")

//2. vars
let x = 5
const y = 6 // קבוע שאסור לשנות אם אני משנה אותו בשורות הבאות יהיה רשום אירור 
console.log(x)
console.log(y)


//3. input 
//1+1 = 2
number1 = +prompt("enter num1") // + הופך אותו ל int
console.log(number1)
number2 = +prompt("enter num2")
console.log(number2)
let solution = number1+number2
console.log(solution)

// //1+1 = 11 כי אין פלוס 
// number1 = prompt("enter num1") 
// console.log(number1)
// number2 = prompt("enter num2")
// console.log(number2)
// let solution2 = number1+number2
// console.log(solution2)


// if else
if (number1 > number2){
    alert(number1 + " bigger then " + number2)
}
else if (number2 > number1){
     alert(number2 + " bigger then " + number1)
}
else if (number1==number2){
    alert(number2 + " equal " + number1)
}

//for
console.log("=====for output======")
for (let i = 0; i < 30; i++)
    console.log(i+1)

// while
console.log("=====while output======")
let j = 0
while (j < 150){
    console.log(j+1)
    j++
}