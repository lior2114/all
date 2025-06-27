// תכנות לא נכון לא יעבוד כי בזמן שזה מחכה 2 שניות ה try  catch פועלים מה שאין להם מה לתפוס או מה לשדר
//error
function randomNumber() {
    setTimeout(() => {
        let number = Math.floor(Math.random() * 100)
        if (number > 50) {
            throw number + ":error random number"
        }
        else {
            console.log(number)
        }
    }, 2000);
}
try {
    randomNumber()
}
catch (err) {
    console.log(err);
}
console.log("continue...");




//אי אפשר try catch בתכנות אנסינכורני
// פתרון 1
function handleError(err) {
    console.log(err)
}

function randomNumber(callback) {
    setTimeout(() => {
        let number = Math.floor(Math.random() * 100)
        if (number > 50) {
            let err = number + ":error random number"
            callback(err) // הגדרת משתמש שהוא פונקציה על ידי סוגרים כדי שיקבל רק פונקציות
        }
        else {
            console.log(number)
        }
    }, 2000);
}

randomNumber(handleError)



// פתרון 2 
function handleErrorCallback(err) {
    console.log("Callback Error:", err);
}

function handleSuccessCallback(number) {
    console.log("Callback Success:", number);
}

function randomNumberWithCallbacks(successCallback, errorCallback) {
    setTimeout(() => {
        let number = Math.floor(Math.random() * 100);
        if (number > 50) {
            let err = number + ":error random number";
            errorCallback(err);
        } else {
            successCallback(number);
        }
    }, 2000);
}

randomNumberWithCallbacks(handleSuccessCallback, handleErrorCallback);
console.log("hello world") // יופיע ראשון כי כל מה שרשמנו לפניו יופעל רק אחרי 2  שניות 