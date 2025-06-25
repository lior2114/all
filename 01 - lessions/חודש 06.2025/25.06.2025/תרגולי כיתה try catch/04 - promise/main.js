//תבנית של פרומיס
function f(){
    let p = new Promise((resolve, reject) => {
        
    });
    return p;
}


//תרגיל של פרומיס
function randomNumber() {
    // פרומיס היא פונקציה שמקבלת 2 פונקציות אחת של טיפול בהצלחה ואחת של טיפול בשגיאה
    let p = new Promise((resolve, reject) => {
        let number = Math.floor(Math.random() * 100)
        if (number > 50) {
            resolve("success random number")
        }
        else {
            reject("error random number");
        }
    });
    return p;
}

//. () =>{}

let solution = randomNumber()
solution
    .then((success) => { console.log(success) })
    .catch((err) => { console.log(err) })