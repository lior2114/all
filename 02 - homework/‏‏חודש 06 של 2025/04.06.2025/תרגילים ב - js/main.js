// function number1_10(){
//     let i = 1
//     while (i < 11) {
//         console.log(i)
//         i++
//     }
// }
// number1_10()

// function active_name(){
//     let name = prompt("enter name: ")
//     while (name != "admin"){
//         name = prompt("enter name: ")
//     }
// }
// active_name()

// function equwal_number(){
//     let number = +prompt("enter number: ")
//     while (number%2 ==1){
//         number = +prompt("enter number: ")
//     }
// }

// equwal_number()

// function numbers_with_3(){
//     let i = 1;
//     while (i < 51) {
//         if (i.toString().includes('3')) {
//             console.log(i);
//         }
//         i++;
//     }
// }
// numbers_with_3();

// function sum_number(){
//     let num = +prompt("enter number:  ");
//     let summ = 0;
//     num = Math.abs(num); // handle negative numbers
//     while (num > 0) {
//         summ += num % 10;
//         num = Math.floor(num / 10);
//     }
//     console.log(summ);
// }

// sum_number()

// function number_number(){
//     let num = +prompt("enter number:  ");
//     let summ = 0;
//     num = Math.abs(num); // handle negative numbers
//     while (num > 0) {
//         summ += 1;
//         num = Math.floor(num / 10);
//     }
//     console.log(summ)
// }

// number_number()

// function skip_split_4(){
//     for (let i = 20;i < 41; ) {
//         if (i % 4 == 0) {
//             i++;
//         }
//         else {
//             console.log(i++);
//         }
//     }
// }
// skip_split_4()


//36
// function revese_name(){
//     let name = prompt("enter name: ")
//     let revese = '';
//     for (let i = name.length - 1; i >= 0; i--){
//         revese += name[i]
//     }
//     console.log(revese)
// }
// revese_name()


function number_split(){
    let num = document.getElementById("number").value
    if (num %2 == 0){
        alert ("number split")
    }
    else{
        alert("dont split")
    }

}