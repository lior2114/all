let arr = [10,20,30,40,50]
sum = 0
for (let i = 0; i<arr.length; i++ ){
    sum += arr[i]
}
console.log(sum)
let avg = sum/arr.length
console.log(avg)

let arr2 = []
for (let i = 0; i<2; i++){
let number = +prompt("enter number " + i +":")
arr2.push(number)
}
console.log(arr2)