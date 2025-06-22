function printName() {
    console.log("oren")
}

function printAdress() {
    console.log("telaviv")
}

function fireMan() {
    console.log("fire fire")
}

function policeMan() {
    console.log("police police hands up")
}
function f(callback) {
    callback() //הפעלת פונקציה מתבצעת בסוגרים אז מגדירים משתנה ואז שמים אותו בסוגרים ככה שהוא יעבוד רק ששולחים לו פונקציה והוא יציג אותה 
}


f(printName)
f(printAdress)
f(fireMan)
f(policeMan)