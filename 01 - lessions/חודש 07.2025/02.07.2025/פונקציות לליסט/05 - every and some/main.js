let arr = [1,2,3,4,5,100,200,204,1000,3000,3001,3002,4000];

//every
//בודק תנאי של כל המערך ומחזיר אמת או שקר 
let answer = arr.every((item) => item > 100);
console.log(answer); // false

//some
//בודק לי אם יש אחד לפחות שקיים 
let answer2 = arr.some((item) => item > 100);
console.log(answer2); // true