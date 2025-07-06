let arr = [1,2,3,4,5,100,200,204,1000,3000,3001,3002,4000];


//השיטה ארוכה 
let newArr = [];
for(let i=0; i<arr.length; i++){
    if(arr[i] > 100){
        newArr.push(arr[i]);
    }
}

console.log(newArr);

//פילטר זה עם תנאי ומסנן לפי התנאי 
//עם פילטר 
let newArr2 = arr.filter((item) => item > 100);
console.log(newArr2);

//זוגי
let evenArr = arr.filter((item) => item % 2 === 0);
console.log(evenArr);

//אי זוגי
let oddArr = arr.filter((item) => item % 2 == 1);
console.log(oddArr);