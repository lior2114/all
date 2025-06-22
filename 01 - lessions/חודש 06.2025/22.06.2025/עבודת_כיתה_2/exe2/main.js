function cool(callback) {
	callback();
}

function random_num(){
    return console.log(Math.floor(Math.random()*100))
}
cool(random_num)