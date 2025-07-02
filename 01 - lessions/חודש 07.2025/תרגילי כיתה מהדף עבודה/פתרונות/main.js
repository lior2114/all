let lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];

//שאלה ראשונה
let newlis1 = lis.filter ((split) => split%2 == 0)
console.log(newlis1)


// שאלה 2
let doublelis = lis.map((double) => double * 3)
console.log(doublelis)


// שאלה 3
let namelis = [
    "Noa", "Liam", "Maya", "Daniel", "Yael", "David", "Tamar", "Eitan", "Shira", "Amit",
    "Omer", "Gal", "Roni", "Yarden", "Nadav", "Lior", "Dana", "Tal", "Itay", "Hila"
];
namelis.forEach((item)=>{
    console.log(item) //יציג לי כל שם בשורה בנפרד
})


// שאלה 4
let findlis = lis.find((item) => item % 5 == 0)
console.log(findlis)


// שאלה 5
let somelis = lis.some((item) => item < 0)
console.log(somelis) //false כי אין מספר שלילי במערך 

// שאלה 6
let everylis = lis.every((item) => item>0)
console.log(everylis) //true כי כל המספרים במערך גדולים מ 0 

// שאלה 7
let fruitlis = ["apple", "banana", "orange"]
let indexof = fruitlis.indexOf("banana")
console.log(indexof)
 