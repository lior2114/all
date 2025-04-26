hours_week = int(input("enter your hours per week: "))
salaryh = float(input("enter your salary per hour: "))

if hours_week > 40:
    print ("your salary is: ", (salaryh * hours_week)*1.5)

else:
    print ("your salary is: " , salaryh * hours_week)
