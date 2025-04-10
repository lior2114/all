import random
print("==========A=========")
def random_numbers(len_ran):
    lis = []
    for i in range(len_ran):
        n = random.randint(1,100) 
        lis.append(n)
    return lis

print("==========B=========")
for i in range(3):
    len_list = int(input("enter number for len list: "))
    x = random_numbers(len_list)
    print(x)