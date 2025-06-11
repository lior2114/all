let electricities =  {
    123: "microwave",
    321: "refrigerator",
    456: "washing machine",
}

let code = +prompt("enter product code: ")
let namee = prompt("enter product name: ")

electricities[code] = namee
console.log(electricities)

let search_by_key = +prompt("enter code to serach for product: ")
if (search_by_key in electricities){
    alert("yes exist: " + electricities[search_by_key])

}
else{
    alert("not exists")
}

for (let key in electricities){
    console.log("Product_id: "+ key + ", " + "Product Name: " + electricities[key])

}

let delete_key = +prompt("enter code to delete product: ")
delete electricities[delete_key]
console.log(electricities)