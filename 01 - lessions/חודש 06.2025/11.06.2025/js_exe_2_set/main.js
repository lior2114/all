// הגדרת סט 
function set(){
    let arr = new Set()
    for (let i = 0; i< 5; i++){
        let number = +prompt("enter num ")
        arr.add(number)
    }
    arr.add("hello")
    console.log(arr)

    if (arr.has(3)){
        alert("3 exists")
    }

    if (arr.has("hello")){
        alert("hello exists")
    }

    if (arr.has(100)){
        alert("remove 100")
        arr.delete(100)
    }
}
set()

// הפיכת מחרוזת לסט 
function test() {
    let arr = [1, 2, 3, 4, 1, 2, 2, 3, 3, 3];
    let s = new Set(arr);
    console.log(s); // 1,2,3,4

    // add
    s.add(5);
    console.log(s);

    // delete
    s.delete(2);
    console.log(s);

    // has
    console.log(s.has(3)); // true
}

test();

// סריקת סט
function scan(){
    let items = new Set()
    for(let i=0;i<10000;i++){
        let number = Math.floor(Math.random()*100)
        items.add(number)
    }

    for(let item of items){
        console.log(item)
    }
}
scan()