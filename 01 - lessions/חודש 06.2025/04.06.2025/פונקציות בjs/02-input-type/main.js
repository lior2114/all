function isEven(){
    let num = document.getElementById("number").value
    if (typeof num === "string" && isNaN(Number(num))) {
        document.getElementById("answer").innerText = "num is string";
    }
    else if (Number(num) % 2 == 0) {
        document.getElementById("answer").innerText = "Even";
        document.getElementById("answer").style.color = "yellow";
    }
    else if (Number(num) % 2 != 0) {
        document.getElementById("answer").innerText = "Odd";
        document.getElementById("answer").style.color = "red";
    }
}