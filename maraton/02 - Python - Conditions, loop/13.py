first = int(input("enter first: "))
last = int(input("enter last: "))
num = int(input("enter num: "))

for first in range(last):
    if first % num == 0:
        print(first+1)
    