function cool(paintCallback) {
	paintCallback();
}

function randomColor(){
    let colors = ["red", "blue","green", "yellow"];
    return console.log(Math.floor(Math.random()*colors.length))
}

cool(randomColor)