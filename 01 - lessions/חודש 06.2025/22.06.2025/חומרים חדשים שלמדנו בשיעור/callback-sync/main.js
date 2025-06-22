console.log("start")
setInterval(()=>{
    console.log("hi hi good pizza ordered")
}, 5000)
console.log("end")

//start , end , hi hi good pizza ordered


function stam() {
    counter = 0
    setInterval(() => {
        counter++
        console.log(counter)
    }, 1000) // every second
}

stam()