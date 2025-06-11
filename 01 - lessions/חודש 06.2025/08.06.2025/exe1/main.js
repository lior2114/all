// ====1====
function number0_200(){
    let lis = []
    let i = 0;
    while(i < 100) {
        let num = Math.floor(Math.random() * 200)
        lis.push(num)
        i++;
    }
    console.log(lis)
    console.log("lis length: "+lis.length)
    return lis;
}
let lis = number0_200()
// ====2====
function if_number_on_list(){
    let number = +prompt("enter number to check if in list: ")
    if (lis.indexOf(number)>=0){
        alert ("yes number in the list")
    }
    else{
        alert("number not on the list")
    }
}

function count_number(){
    let numbers = lis
    let number = +prompt("enter number to know how many time he on the list: ")
    let counter = 0 
    for (let i = 0 ; i<numbers.length; i++){
        if (numbers[i]== number){
            counter++
        }
    }
    alert(counter)
}