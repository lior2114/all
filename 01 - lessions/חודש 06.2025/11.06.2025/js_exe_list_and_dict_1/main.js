//תרגיל 1
// let cars = [
//     { brand: "Toyota", model: "Corolla", year: 2020, color: "white" },
//     { brand: "Honda", model: "Civic", year: 2019, color: "black" },
//     { brand: "Mazda", model: "3", year: 2021, color: "red" }
// ];
// // הצגת כל אובייקט, כל מאפיין בשורה נפרדת
// for (let car of cars) {
//     for (let key in car) {
//         console.log(key + ": " + car[key]);
//     }
//     console.log("-----");
// }
// console.log("-----");
// // הצגת כל אובייקט ע"י לולאה מקוננת
// for (let car of cars) {
//     for (let key in car) {
//         console.log(car[key]);
//     }
//     console.log("-----");
// }
// 3 דרכים להרצה
// for(let item of cars){
//     //console.log(item)
//     console.log(item.model + " " + item.year + " " + item.color + " " + item.brand)
// }
// console.log("==============================================")
// //item is index
// for(let i in cars){
//     console.log(cars[i].model + " " + cars[i].year + " " + cars[i].color + " " + cars[i].brand)
// }
// console.log("==============================================")

// //for(let i=0;i<cars.length;i++)
// for(let i=0;i<cars.length;i++ ){
//     console.log(cars[i].model + " " + cars[i].year + " " + cars[i].color + " " + cars[i].brand)
// }


// תרגיל 2
let clothes = [
    { type: "Shirt", size: "M", color: "blue", price: 100 },
    { type: "Pants", size: "L", color: "black", price: 150 },
    { type: "Jacket", size: "S", color: "green", price: 200 },
    { type: "Dress", size: "M", color: "red", price: 250 },
    { type: "Skirt", size: "S", color: "yellow", price: 80 }
];

summ = 0
counter = 0
for (let key in clothes[0]) {
    console.log(key);
}
for (let item of clothes) {
    summ += item.price;
    counter += 1;
}
avg = summ/ counter 
console.log(avg)


// in - אינדקסים 
//of - מיקומים