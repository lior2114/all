function fname_by_color(){
    let name = document.getElementById("fname").value
    if (name[0]== "a" || name[0] == "A"){ // אפשר גם name[0].toLowerCase()==="a"
        document.getElementById("firstname").innerText = name
        document.getElementById("firstname").style.color = "green"
    }
    else{
        document.getElementById("firstname").innerText = name
        document.getElementById("firstname").style.color = "red" 
    }
}