function generateCuteAnimalAfterDelayAsync(){
    let p = new Promise((resolve, reject) => {
        setTimeout(() => {
            let cute_lis = ["חתלתול", "כלבלב", "ארנבון", "תוכון"];
            let uncute_lis = ["עקרב", "עכביש", "ג'וק"];
            let long_lis = cute_lis.concat(uncute_lis);
            let random_index = Math.floor(Math.random() * long_lis.length);
            let selected_word = long_lis[random_index];
            if (cute_lis.includes(selected_word)) {
                resolve("cute animal " + selected_word);
            } else {
                reject("not cute " + selected_word);
            }
        }, 10);
    });
    return p;
}


function click_activation(){
    let show_div = document.getElementById('result')
    generateCuteAnimalAfterDelayAsync()
    .then ((success)=>{show_div.textContent=success})
    .catch ((fail)=>{show_div.textContent = fail })
}