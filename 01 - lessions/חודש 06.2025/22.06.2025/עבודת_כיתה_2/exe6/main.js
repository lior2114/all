function amazing(paintCallback) {
	const paintedColor = paintCallback("Red", "Green", "Blue");
	document.write("Painted Color: " + paintedColor);
    document.body.style.backgroundColor = paintedColor;
}


function some_colors(colorA, colorB, colorC){
    let arr = [colorA, colorB, colorC]
    return arr[Math.floor(Math.random()*arr.length)]
}

amazing(some_colors)