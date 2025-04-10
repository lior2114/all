# א
salary1 = int(input("enter the first salary: "))
salary2 = int(input("enter the second salary: "))
salary3 = int(input("enter the third salary: "))
salary4 = int(input("enter the fourth salary: "))
salary5 = int(input("enter the fifth salary: "))
salary6 = int(input("enter the sixth salary: "))
totalsalary = (salary1,salary2,salary3,salary4,salary5,salary6)

#ב
avg = sum(totalsalary)/len(totalsalary)
print(f"the average salary is: {avg}")

#ג
maxsalary = totalsalary[0]
for salary in totalsalary:
    if salary > maxsalary:
        maxsalary = salary
print(f"the highest salary is: {maxsalary}")

print(f"The highest salary is: {max(totalsalary)}")

#ד
minsalary = totalsalary[0]
for salary in totalsalary:
    if salary < minsalary:
        minsalary = salary
print(f"the lowest salary is: {minsalary}")

minsalary = min(totalsalary)


