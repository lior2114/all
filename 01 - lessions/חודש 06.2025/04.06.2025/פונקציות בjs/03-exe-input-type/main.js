function colorful_name(){
   let name = document.getElementById("Fname").value
if (name.length == 0)
    return alert ("name is empty")
if (name[0].toLowerCase() === 'a'){ //אפשר גם name[0]=='a'
    document.getElementById("answer").innerText = name
    document.getElementById("answer").style.color = "green"
    document.getElementById("Fname").style.backgroundColor = "green"
}
else{
    document.getElementById("answer").innerText = name
    document.getElementById("answer").style.color = "red"
    document.getElementById("Fname").style.backgroundColor = "red"
}
document.getElementById("Fname").value = ""//מאפס את המשתנה לכלום 
}