first = int(input("enter first: "))
last = int(input("enter last: "))
num = int(input("enter num: "))

if last >= first:
    for first in range(first,last+1):
        if first % num == 0:
            print(first)
else:
    for last in range(last,first+1):
        if last % num == 0: 
            print(last)

        