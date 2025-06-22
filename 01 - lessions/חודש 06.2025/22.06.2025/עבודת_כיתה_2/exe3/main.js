function nice(callback) {
	callback(42);
}

function print_num(num){
    return console.log(num)
}

nice(print_num)