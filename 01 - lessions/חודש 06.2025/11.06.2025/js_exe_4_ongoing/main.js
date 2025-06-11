// a-d
// let car = {
//     brand: "Toyota",
//     model: "Corolla",
//     year: 2022
// };

// console.log(car.brand);
// console.log(car.model);
// console.log(car.year);

// car.color ="Red"
// car.year = 2025
// delete car.model
// console.log(car)


//e כתוב פונקציה שמקבלת אובייקט student עם מאפיינים name, grade, ומדפיסה:
// שם התלמיד: X, ציון: Y
// function clas(student){
// console.log("name of the student: " + student.namee + " grade: " + student.grade)
// }

// let s = {
//     namee:"lior",
//     grade:100
// }
// clas(s)


// f צור אובייקט בשם book עם מפתחות: title, author, pages.
//  כתוב לולאת for...in שמדפיסה את כל המפתחות והערכים שלו.
// let book = {
//     title: "JavaScript Basics",
//     author: "John Doe",
//     pages: 250
// }

// for (let categories in book){
//     console.log(categories + " : "+ book[categories])
// }


//g  כתוב פונקציה שמקבלת אובייקט ומחזירה את מספר המפתחות בו.
// function countKeys(obj) {
//     return Object.keys(obj).length;
// }

// console.log(countKeys(book)); // ידפיס 3


//h צור מערך של אובייקטים בשם products.
//  כל אובייקט מייצג מוצר עם name, price, inStock.
//  הדפס את שמות כל המוצרים שנמצאים במלאי (inStock === true).
// let products = [
//     { name: "Laptop", price: 3500, inStock: true },
//     { name: "Mouse", price: 100, inStock: false },
//     { name: "Keyboard", price: 250, inStock: true }
// ];
// for (let key in products){
//     if (products[key].inStock == true){
//         console.log(products[key].name)
//     }
// }


//i כתוב פונקציה שמקבלת אובייקט שבו מפתחות הם שמות תלמידים וערכים הם ציונים.
//  הפונקציה תחזיר את השם של התלמיד עם הציון הגבוה ביותר.
// function printStudentGrades(students) {
//     let max = 0
//     let max_name = ""
//     for (let name in students) {
//         console.log("Student: " + name + ", Grade: " + students[name]);
//         if (students[name]> max){
//             max = students[name]
//             max_name = name
//         }
//     }
//     return console.log("Max Grade is: " + max + ", " + "of the Student: " + max_name)
// }

// let students = {
//     "Lior": 100,
//     "Dana": 88,
//     "Noam": 76,
//     "Yael": 95,
//     "Amit": 84,
//     "Tamar": 91
// };
// printStudentGrades(students);


//j צור אובייקט בשם dictionary עם מילים באנגלית כמפתחות, והתרגום לעברית כערכים.
//  כתוב פונקציה שמקבלת מילה באנגלית ומחזירה את התרגום לעברית מתוך ה־dictionary.
//  אם המילה לא קיימת, תחזיר "לא נמצא".
function translate(words){
    let dictionary = {
        my_name : "השם שלי",
        age: "גיל",
        car: "מכונית",
        book: "ספר",
        student: "תלמיד",
        grade: "ציון",
        author: "מחבר",
        title: "כותרת",
        pages: "עמודים",
        price: "מחיר",
        inStock: "במלאי"}
    if (words in dictionary){
        return console.log(dictionary[words])
    }
    else{
        alert("the word not exists in the dictionary")
    }
}
let word = prompt("enter your word to translate: ")
translate(word)


// כל מיני דוגמאות להצגה של הדברים 
// for (let i = 0; i < products.length; i++) {
//     console.log(products[i]["name"]);
//     console.log(products[i]["price"]);
//     console.log(products[i]["inStock"]);
// }

// for (let i = 0; i < products.length; i++) {
//     console.log(products[i].name);
//     console.log(products[i].price);
//     console.log(products[i].inStock);
// }

// for (let i = 0; i < products.length; i++) {
//     let product = products[i];
//     console.log(product.price);
//     console.log(product.inStock);
//     console.log(products[i]["inStock"]);
// }