function randomNumber() {
    let number = Math.floor(Math.random() * 100);
    if (number > 50) {
        throw number + " error random number"; // throw
    }
    else{
        return number // return
    }
}

try{ // return
    let x = randomNumber()
    console.log(x)
}

catch(err){ // throw גם אם יש 100 פונקציות ברגע שיהיה אירור אחד זה יעצור וידפיס איפה שיש את האירור 
    console.log(err)
}