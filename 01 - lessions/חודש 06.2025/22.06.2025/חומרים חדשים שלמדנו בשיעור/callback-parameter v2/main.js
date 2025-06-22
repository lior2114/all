function random1(min, max) {
    let n = min + Math.floor(Math.random() * (max - min));
    return n
}
//אופציה א 
function s(callback) {
   let x = callback(40, 60);
   console.log(x)
}
// אופציה ב
function f(callback , min,max) {
   let x = callback(min, max);
   console.log(x)
}

//לאופציה א 
s(random1)

//לאופציה ב
f(random1,5,100);



// אפשר גם להעביר פונקציה אנונימית
s(function(min, max) {
    return min + max;
});

// או חץ
f((min, max) => min * max, 2, 8);