let arr = [1, 2, 3]
let arr2 = arr //reference שזה מצביע על אותו מקום בקוד 
arr2[0] = 1000
console.log(arr) // arr2 משתנה
// copy array
let newArr = []
for (let i = 0; i < arr.length; i++) {
    newArr.push(arr[i])
}
newArr[0] = 1000


//לא ישנה את המערך הרגיל אלא משכפל אותו ומשנה בשכפול שלו ולא במקורי 
let arr3 = [...arr]
arr3[2] = 5000
console.log(arr)   // [1000, 2, 3] כשנדפיס את הרגיל  זה ישאר רגיל 
console.log(arr3)  // [1000, 2, 5000] שנדפיס את הקופי זה ישנה אותו לפי מה ששינינו


//--------------------------clone arr  ================
let copyArr = [...arr]; // spread operator
copyArr[2]= 5000
console.log(arr)
console.log(copyArr)

let friends = ["uri", "shosi"]
let copyFriend = [...friends]

//--------------------------merge arr  ================
let a = [1,2,3]
let b = [10,20,30]
let notmerge = [a,b] // [[1,2,3], [10,20,30]]
let merge = [...a, ...b] // [1,2,3,10,20,30]
console.log(notmerge)
console.log(merge)

//--------------------------add items  ================
let nums = [2,3,4]
let addNums1 = [1, ...nums] // [1,2,3,4]
let addNums2 = [...nums, 5] // [2,3,4,5]