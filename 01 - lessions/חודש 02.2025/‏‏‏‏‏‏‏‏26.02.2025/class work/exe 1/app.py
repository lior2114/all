import listmodule

my_numbers = listmodule.do_list(1,10)
print(f"your list is: {my_numbers}")

s = listmodule.sum_list(my_numbers)
print(f"the sum of your list is: {s}")

a = listmodule.avg(my_numbers)
print(f"your list avarage is: {a}")

#אם הפונקציה מחזירה שתי משתנים אז משווים אותם להצגה שלה 
l, counter = listmodule.split(my_numbers)
print(f"your split numbers are {l}, and it has {counter} of splits numbers")