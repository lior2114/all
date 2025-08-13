let person = {
    firstname: "oren",
    lastname: "uziel",
    password: "123"
}

person = {...person, lastname: "davidd", age: 4}
function h(e){
    console.log(e.target.value)
    person = {...person, [e.target.name]:e.target.value}
    // console.log(person)
}



function f(e){
    console.log(e.target.value)
    person = {...person, [e.target.name]:e.target.value}
    console.log(person)
}

function g(e){
    alert(e.target.value)
    alert(e.target.name)
    person = {...person, [e.target.name]:e.target.value}
    console.log(person)
}
