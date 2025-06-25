
// A
function call_success(len_word){
    alert("success the length is: " + len_word)
}

function call_error(len_word){
    alert("error the length is: " + len_word)
}

function len_lis(word, success, error){
    setTimeout(()=>{
        let len_word = word.length
        if (len_word>5){
            success(len_word)
        } else{
            error(len_word)
        }

    }, 5000)
}

let word = "wordess"
len_lis(word,call_success,call_error)


//B
function handleSuccess(name) {
    alert(name);
}

function handleError(err) {
    alert(err);
}

function isBiggerThan5(successCallback, errorCallback) {
    setTimeout(() => {
        let name = prompt("enter your name");
        if (name.length > 5) {
            successCallback("success enter your name");
        } else if (name.length > 0 && name.length < 5) {
            errorCallback("error. name has to be longer than 5 characters");
        } else if (name.length == 0) {
            errorCallback("error. name cant be than 0 characters");
        }
    }, 5000);
}

isBiggerThan5(handleSuccess, handleError);