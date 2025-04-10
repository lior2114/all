import random
lis = set()
counter = 0 
while counter != 14:
    if len(lis) < 6:
        num = random.randint(1,37)
        lis.add(num)
    else:
        for n in lis:
            print(n,end =" ")
        lis.clear()
        print()
        counter += 1