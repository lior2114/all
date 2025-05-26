//1
// let num = +prompt("enter number: ");
// console.log(num * num);

//2
// let firstName = prompt("enter your name: ")
// for (let i = 0; i<5; i++){
//     console.log(firstName)
// }


//3
// let age = +prompt("enter your age: ")
// if (age < 18 || age < 0){
//     console.log("you cant enter cinema!")
// }

// else{
//     console.log("you can enter cinema:)")
// }

//4
// for (let i = 65; i <= 90; i++) {
//     console.log(String.fromCharCode(i));
// }

//5
// let names_arr = []
// for (let i = 0; i<5; i++){
//     n = prompt("enter your " + i + "name: ")
//     names_arr.push(n)
// }
// console.log(names_arr)

//6
// for  (let i = 1; i<31; i++){
//     if (i%7 ==0){
//         console.log("boom")
//     }
//     else{
//         console.log(i)
//     }
// }

//7
// for (let i = 1; i <11; i++){
//     console.log(Math.floor(Math.random()* 100))
// }


//8
// let randomWords = ["apple", "banana", "cat", "dog", "elephant", "flower", "guitar", "house", "island", "jungle"];
// for (let i = 0; i < randomWords.length; i++) {
//     for (let j = 0; j < randomWords[i].length; j++) {
//         console.log(randomWords[i][j]);
//     }
// }


//9
// let choose_number = +prompt("enter number: ")
// if (choose_number % 2 == 0 && choose_number % 3 == 0){
//     console.log("the number split in 2 and 3")
// }
// else{
//     console.log("it doesnt split:(")
// }

//10
// let i = 1;
// while (i < 11) {
//     console.log(i);
//     i++;
// }

//11
// let primnary_name = "admin"
// let user_chooise = prompt("enter name: ")
// while (primnary_name != user_chooise){
//     console.log("only admin")
//     user_chooise = prompt("enter name: ")
// }
// alert("you are in :)")


// //12
// let user_chooise2 = +prompt("enter number: ")
// while(user_chooise2 % 2 != 0){
//     user_chooise2 = +prompt("enter number")
// }
// alert("yes the number is split in 2 :)")

//13
// let i = 1;
// while (i<101){
//     console.log(i);
//     i++;
// }

//14
// let i = 1;
// while (i < 1000) {
//     if (i.toString().includes('3')) {
//         console.log(i);
//     }
//     i++;
// }

//15
// let user_number = +prompt("enter number: ");
// let number_length = 0;
// let temp_number = Math.abs(user_number); // handle negative numbers
// if (temp_number === 0) {
//     number_length = 1;
// } else {
//     while (temp_number > 0) {
//         number_length += 1;
//         temp_number = Math.floor(temp_number / 10);
//     }
// }
// console.log(number_length);

//16
// for (let i = 1; i < 101;){
//     if (i%2 == 0){
//         console.log(i);
//         i++;
//     }
//     else{
//         console.log(i + "*");
//         i++;
//     }
// }


//17
// for (let i = 20; i < 40;){
//     if (i%4 == 0){
//         i++;
//     }else{
//         console.log(i);
//         i++
//     }
// }

//18
// let user_number2 = +prompt("enter number: ");
// for (let i = 0; i < user_number2+1; i++){
//     console.log(i)
// }

//19
// let choose_name = prompt("enter a word: ")
// let words = ""
// for (let i = choose_name.length - 1; i >= 0; i--) {
//     words += choose_name[i];
// }
// console.log(words)

//20
// let user_number3 = +prompt("enter number: ")
// for (let i = user_number3; i>=0; i--){
//     console.log(i)
// }