//שלושה דרכים להגדיר פונקציה בגווה סקריפט 

function sum1(a, b) {
    let sum = a + b
    return sum
}

//declaraion
const sum2 = function (a, b) {
    let sum = a + b
    return sum
}

//arrow function = פונקצית חץ 
const sum3 = (a, b) => {
    let sum = a + b
    return sum
}

let x1 = sum1(1, 1)
let x2 = sum2(2, 2)
let x3 = sum3(3, 3)
console.log(x1)
console.log(x2)
console.log(x3)