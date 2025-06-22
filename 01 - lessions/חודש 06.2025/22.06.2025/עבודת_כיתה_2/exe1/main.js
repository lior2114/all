function my_name(){
    return console.log("lior")
}

function f(callback){
    callback()
}
f(my_name)