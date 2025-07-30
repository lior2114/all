console.log("-------destructure--------")
const person = { namee: "Dana", age: 50 };
// const name = person.name;
// const age = person.age;
const { namee, age } = person; // בסוגרים הסדר של המילים לא משנה כי הוא קולט אותם לפי תאימות המילים 
console.log(person);
console.log(namee);
console.log(age);

//לא לפי הסדר
const student = { firstName: "John", lastName: "Doe", grade: 85 };
const { firstName, grade, lastName } = student;
console.log(firstName); // "John"
console.log(lastName);  // "Doe"
console.log(grade);     // 85

console.log("-------array destructure acording to index--------")
const colors = ['red', 'green', 'blue'];
const [firstColor, secondColor, memo] = colors; // כאן משנה הסדר לא השמות כי הוא עובד לפי אינדקס
console.log(firstColor);  // 'red'
console.log(secondColor); // 'green'