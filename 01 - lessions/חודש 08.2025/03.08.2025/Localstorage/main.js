function saveUser(){
    let username = document.getElementById("username").value
    let email = document.getElementById("email").value

    localStorage.setItem("username", username)
    localStorage.setItem("email", email)

    alert (username + ": has been saved")
     alert (email + ": has been saved")
}


function logData(){
    let username = localStorage.getItem("username")//לוקאל סטורג נשמר באופן כללי וממה שנשמר בו אפשר להשתמש בלי לשלב פונקציות 
    let email = localStorage.getItem("email")
    console.log("username: " + username)
    console.log("email: "+ email)
}

function saveObject(){
    const user = {nameing :"lior", age: "23"}
    localStorage.setItem("user", JSON.stringify(user)) //רק עם יש לי דיקשינרי של דברים אז ככה שומרים אותו 
}

function getObject(){
    const struser =localStorage.getItem("user")
    console.log(struser) //וככה מחלצים אותו (המשך שורה 22)
    const user = JSON.parse(struser) // וככה מחלצים אותו לאובייקטים 
    console.log(user.nameing)//כמו ככה
    console.log(user.age)
}




function deleteold(){
    localStorage.removeItem("username")
    alert("username has been cleard")
}