function generateWorkingDayAfterDelayAsync(){
    let p = new Promise((resolve,reject)=> {
        setTimeout(() => {
            let good_list = ["ראשון", "שני", "שלישי", "רביעי", "חמישי"]
            let rej_list = ["שישי","שבת"]
            let long_list = good_list.concat(rej_list)
            let choosen_index = Math.floor(Math.random()*long_list.length)
            let choosen_day = long_list[choosen_index]
            if (good_list.includes(choosen_day)){
                resolve ("success the day is: " + choosen_day )
            }
            else {
                reject ("fail the day is: " + choosen_day)
            }
        },100);
    })
    return p;
}

function activate_click1(){
    let answer_div = document.getElementById('result')
    generateWorkingDayAfterDelayAsync()
    .then ((success)=>{answer_div.textContent = success})
    .catch((fail) => {answer_div.textContent = fail})

}