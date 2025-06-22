function random1(min, max) {
    let n = min + Math.floor(Math.random() * (max - min))
    return n 
}

function f(callback, m) {
    let x = callback(40, 60)
    console.log(x) 
}
f(random1)
