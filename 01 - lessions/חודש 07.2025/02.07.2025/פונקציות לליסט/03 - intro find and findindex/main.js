let arr = [1,2,3,4,5,100,200,204,1000,3000,3001,3002,4000];

//find מוצא את האיבר הראשון שעולה 
let num = arr.find((item) => item > 1000);//האיבר הראשון שיתור גדול מ 1000 הוא 3000 אז הוא יחזיר 3000
console.log(num);

//לפי אינדקס 
let index = arr.findIndex((item) => item > 1000); //index is 9
console.log(index);
