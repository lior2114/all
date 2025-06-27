function getArrayFromServerAsync(size){
    let p = new Promise ((resolve,reject) =>{
        setTimeout(() => {
            if (size <= 0){
                reject("Enter positive size")
            }
            let n = Math.floor(Math.random()*100)
            let empty_lis = []
            if (n%2 == 0){
                for (let i = 0; i<size; i++){
                    let added_n = Math.floor(Math.random()*100)
                    empty_lis.push(added_n)
                }
                resolve ("The number is splited the list is: " + empty_lis)    
            }else{
                reject ("The number not split cant bring the list from the server the number is: " + n)
            }
        }, 10);
    }); return p;
}


function click_activation(){
    let size = parseInt(document.getElementById("Enter_size").value)
    let print_div = document.getElementById('result')
    getArrayFromServerAsync(size)
    .then ((success) => {print_div.textContent=success})
    .catch ((fail) => {print_div.textContent= fail})

}