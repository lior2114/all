function amazing(callback) {
	const num = callback(42, 128, 37, 81, 66);
	console.log("Num: " + num);
}

function t(a,b,c,d,e){
    let arr = [a,b,c,d,e]
    return arr[Math.floor(Math.random() * arr.length)]
}

amazing(t)