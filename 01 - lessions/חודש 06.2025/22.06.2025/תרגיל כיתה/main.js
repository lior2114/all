//פונקציה שמקבלת שני מספרים ומחזירה את המכפלה שלהם
function multiplication1(a, b) {
    let sum = a * b
    return sum
}

const multiplication2 = function (a, b) {
    let sum = a * b
    return sum
}

const multiplication3 = (a, b) => {
    let sum = a * b
    return sum
}


//פונקציה שמקבלת מספר ומחזירה true אם הוא זוגי, אחרת false
function split1(num){
    if (num %2 == 0){
        return true
    }
    return false
}

let split2 = function(num){
    if (num %2 == 0){
        return true
    }
    return false
}

let split3=(num)=>{
    if (num %2 == 0){
        return true
    }
    return false
}


//פונקציה שמקבלת מחרוזת ומחזירה את אורכה
function mhrozt1(m) {
    return m.length
}

let mhrozt2 = function(m){
    return m.length
}

let mhrozt3 = (m)=>{
    return m.length
}




//פונקציה שמקבלת מחרוזת ומחזירה אותה באותיות גדולות
function bigmhrozt1(m){
    return m.toUpperCase()
}
let bigmhrozt2 = function(m){
    return m.toUpperCase()
}

let bigmhrozt3 = (m)=>{
    return m.toUpperCase()
}



//פונקציה שמקבלת שני מספרים ומחזירה את המספר הגדול מביניהם
function bigsmall1 (a,b){
    if (a>b){
        return console.log(a + "is bigger")
    }
    return console.log(b + "is bigger")
}

let bigsmall2 = function (a,b){
    if (a>b){
        return console.log(a + "is bigger")
    }
    return console.log(b + "is bigger")
}

let bigsmall3 = (a,b)=>{
    if (a>b){
        return console.log(a + "is bigger")
    }
    return console.log(b + "is bigger")
}


//פונקציה שמקבלת מערך ומחזירה את האיבר הראשון בו
function mahra1(lis){
    return lis[0]
}

let mahra2 = function(lis){
    return lis[0]
}

let mahra3 = (lis)=>{
    return lis[0]
}


// פונקציה שמקבלת מערך ומחזירה את סכום כל האיברים בו
function sum1(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}

let sum2 = function(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}

let sum3 = (arr) => {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}


// פונקציה שמקבלת שם פרטי ומחזירה את המשפט: "שלום, [שם]"
function hello_name1(n){
    return console.log("hello" + n)
}

let hello_name2 = function(n){
    return console.log("hello" + n)
}

let hello_name3 = (n)=>{
    return console.log("hello" + n)
}

// פונקציה שמקבלת גיל ומחזירה האם האדם בגיר (18 ומעלה).
function above_18_1(age){
    if (age > 18){
        return console.log("is bagir")
    }
    return console.log("is teen")
}

let above_18_2 = function(age){
    if (age > 18){
        return console.log("is bagir")
    }
    return console.log("is teen") 
}

let above_18_3 = (age)=>{
    if (age > 18){
        return console.log("is bagir")
    }
    return console.log("is teen")
}


// פונקציה שמקבלת שני מספרים ומחזירה את הממוצע שלהם
function avg1(a,b){
    summ = a+b
   return console.log( "your avg is: "+summ/2)
}

let avg2 = function (a,b){
    summ = a+b
   return console.log( "your avg is: "+summ/2)
}

let avg3 = (a,b)=>{
    summ = a+b
   return console.log( "your avg is: "+summ/2)
}


