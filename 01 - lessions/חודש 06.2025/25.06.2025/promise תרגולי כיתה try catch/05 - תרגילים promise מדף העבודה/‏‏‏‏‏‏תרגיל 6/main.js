function getPizzaFromServerAsync(){
    let p = new Promise ((resolve,reject)=>{
        setTimeout(() => {
            let random_n = Math.floor(Math.random()*1000)
            if (random_n%2 == 0){
                let koter = Math.floor(Math.random() * (50-10 +1)+10)
                let price = Math.floor(Math.random() * (80-20 + 1) +20)
                let extra = Math.floor(Math.random() * (4-0+1) +0)
                resolve ("Success the Pizza is: koter: " + koter + " price: " +price + " extra: " +extra)
            }else{
                reject("Not success")
            }
        }, 10);
    })
    return p;
}

function Pizza_click_activation(){
    let show_div = document.getElementById('result')
    getPizzaFromServerAsync()
    .then ((success) => {show_div.textContent = success})
    .catch ((fail)=>{show_div.textContent = fail})
}