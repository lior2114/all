//יצירת סט של מספרים בין 0-100 
function Random_1_100(){
    let arr = new Set()
    for (let i = 0; i <100; i++){
        let n = Math.floor(Math.random()*100) 
        arr.add(n)
    }
    let summ = 0
    for (let numbers of arr){
        summ += numbers
        console.log(numbers)
    }
    avg = Math.floor(summ/arr.size)
    alert( "your avg is: " + avg)

    let user_number = +prompt("enter number to check if in set: ")
    if (arr.has(user_number)){
        alert("yes the number is exists in set")
    }
    else{
        alert("not in set")
    }
    for (let number of arr) {
        console.log("Number: " + number + "," + " Power: " + (number * number) + ".");
    }
}

Random_1_100()