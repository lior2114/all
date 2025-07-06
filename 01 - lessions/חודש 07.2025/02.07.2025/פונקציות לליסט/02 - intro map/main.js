let arr = [1,2,3,4,5,100,200,204,1000,3000,3001,3002,4000];

// //דריסת הקיים
// let arr = arr.map((item) => item * item);
// console.log(arr);

//בלי דריסה 
let newPower = arr.map((item) => item * item);
console.log(newPower);


// ההבדל בינה לבין המאפ הוא שהמאפ יוצר ליסט חדש והפוראיץ לא מחזיר מערך חדש אלא משנה אותו
// foreach