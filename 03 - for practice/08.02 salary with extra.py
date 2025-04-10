hours_week = int(input("enter your hours per week: "))
salaryh = float(input("enter your salary per hour: "))
if hours_week > 40:
    noextra = (salaryh * hours_week)
    withextra = (hours_week - 40) * (salaryh * 1.5)
    print ("your salary is: ", noextra , "your overtime hours is:", withextra, "total salary is: " , noextra + withextra)

else:
    print ("your salary is: " , salaryh * hours_week)
