//אופציה א 
function generatePrimeNumberAfterDelayAsync(min,max){
    let p = new Promise((resolve,reject)=>{
        setTimeout(() => {
            let number = Math.floor(Math.random() * (max - min +1)) + min;
            if (number <= 1) {
                reject(number + " Not Prime");
            } else {
                let isPrime = true;
                for (let i = 2; i < number; i++) {
                    if (number % i === 0) {
                        isPrime = false;
                        break;
                    }
                }
                if (isPrime) {
                    resolve(number + " is Prime");
                } else {
                    reject(number + " Not Prime");
                }
            }
        }, 10);
    })
    return p;
}




async function click_to_activate(){// לשים לב להתחלה של הפונקציה שבלעדיה זה לא יעבוד 
    try{
        const min = parseInt(document.getElementById('MinNumber').value)
        const max = parseInt(document.getElementById('MaxNumber').value)
        let show_div = document.getElementById('result')
        show_div.textContent = await generatePrimeNumberAfterDelayAsync(min,max)
    }
    catch(err){ // לתת שם לבעיה 
        let show_div = document.getElementById('result')
        show_div.textContent = err; //מה שלא עובד לשלוח לתוך הדיב 
    }
}




