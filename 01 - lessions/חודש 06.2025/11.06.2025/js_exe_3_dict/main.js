let student = {
    name:"Avi",
    age:17,
    grade:92
}

console.log(student.name)// Avi
console.log(student["name"]) // Avi

student.city = "Dimini" // add key city
//change key age
student.age = 18
//change key age
student.age++
//add key password
student.password = "123456"
console.log(student)

//delete key example
delete student.age
console.log(student) // key age removed

if("name" in student){
    alert("key name exist")
}
else{
    alert("key name not exist")
}

for (let key in student){
    console.log(key)//all exists keys - name,  password, grade , city
    console.log(student[key])// all exists values
}

// כי מחקנו אותו ממקודם 
console.log(student.age)//undefind