// שיטה א בלי רשימה
function inputsalary(){
    let summ = 0
    let counter = 0
    let max = 0
    let min = 0 
    for (let i = 0; i<6; i++){
        let salary = +prompt("enter your salary: ")
        summ += salary
        counter += 1
        if (salary> max){
            max = salary
        }
        if (salary <= min || min === 0){
            min = salary
        }
    }
    avg = summ/ counter
    alert(" your avg is: " + avg +" your max salary is: "+ max + " your min salary is: "+ min)


}
inputsalary()


// שיטה ב עם רשימה ולולאות
function inputsalaryWithList() {
    let salaries = [];
    for (let i = 0; i < 6; i++) {
        let salary = +prompt("enter your salary: ");
        salaries.push(salary);
    }
    let summ = 0;
    let max = salaries[0];
    let min = salaries[0];
    for (let i = 0; i < salaries.length; i++) {
        summ += salaries[i];
        if (salaries[i] > max) {
            max = salaries[i];
        }
        if (salaries[i] < min) {
            min = salaries[i];
        }
    }
    let avg = summ / salaries.length;
    alert(" your avg is: " + avg + " your max salary is: " + max + " your min salary is: " + min);
}
inputsalaryWithList();
