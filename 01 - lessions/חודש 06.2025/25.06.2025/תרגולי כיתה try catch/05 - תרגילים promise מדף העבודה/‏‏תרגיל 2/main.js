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

function click_to_activate(){
    const min = parseInt(document.getElementById('MinNumber').value)
    const max = parseInt(document.getElementById('MaxNumber').value)
    let show_div = document.getElementById('result')
    generatePrimeNumberAfterDelayAsync(min,max)
        .then ((success)=> {show_div.textContent = success})
        .catch((error) => {show_div.textContent = error})
}