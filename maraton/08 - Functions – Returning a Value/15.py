import random
print("==========A=========")
def random_numbers(min,max):
    listed = []
    if max < min: 
        min,max = max,min
    for i in range(min,max):
        if i > 1:
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                listed.append(i) 
    return listed

min_number= int(input("enter min number: "))
max_number = int(input("enter max nubmer: "))
x = random_numbers(min_number,max_number)
print(x)
