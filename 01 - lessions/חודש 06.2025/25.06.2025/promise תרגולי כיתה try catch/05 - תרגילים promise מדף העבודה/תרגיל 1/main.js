
// רגיל דרך מספר שמכניסים 
// function generate7BoomAfterDelayAsync(min,max){
//     let p = new Promise ((resolve, reject) =>{
//         setTimeout(() => {
//             let number = Math.floor(Math.random()*(max-min))
//             if (number % 7 == 0 || number %10 ==7){
//                 resolve("success number split in 7 or end in 7 :)")
//             }else{
//                 reject("error no spilt in 7 and no end in 7")
//             }
//         }, 1000);
//     });
//     return p;
// }

// let result = generate7BoomAfterDelayAsync(7,100)
// result
// .then ((success) => {alert(success)})
// .catch ((error) => {alert(error)})



// עם הכנסה מהדף 
function generate7BoomAfterDelayAsync(min,max){
    let p = new Promise ((resolve, reject) =>{
            let number = Math.floor(Math.random()*(max-min))
            if (number % 7 == 0 || number %10 ==7){
                resolve("success " + number + " split in 7 or end in 7 :)")
            }else{
                reject("error " + number + " not spilt in 7 and not end in 7")
            }
    });
    return p;
}
function handleClick() {
    const min = parseInt(document.getElementById('minInput').value); // אפשר גם להשים ב=במקום pareint  +
    const max = parseInt(document.getElementById('maxInput').value);
    const resultDiv = document.getElementById('result');
    generate7BoomAfterDelayAsync(min, max)
        .then(success => resultDiv.textContent = success)
        .catch(error => resultDiv.textContent = error);
}

