salary1 = int(input("enter the first salary: "))
salary2 = int(input("enter the second salary: "))
salary3 = int(input("enter the third salary: "))
salary4 = int(input("enter the fourth salary: "))
salary5 = int(input("enter the fifth salary: "))
salary6 = int(input("enter the sixth salary: "))
total = (salary1, salary2,salary3,salary4,salary5,salary6)
print(sum(total)/ len(total))

counter = 0 
for i in total: 
    if i > counter:
        counter = i 
print (f"the max salary is: {counter}")

counter2 = total[0]
for j in total:
    if j < counter2:
        counter2 = j
print (f"the lowest salary is: {counter2}")
