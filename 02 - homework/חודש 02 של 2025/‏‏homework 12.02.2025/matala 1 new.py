import random
lis = []

for i in range(100):
    n = random.randint(1,10)
    lis.append(n)
print (lis)

n = int(input("enter a number to know if he exist on the list: "))
if n in lis:
    print("yes")
else:
    print("no")

n2 = int(input("enter a number to know how many times it append on the list: "))
counter = 0 
for i in lis:
    if i == n2:
        counter +=1
    elif n2 not in lis:
        print("number not showing on the list")
        counter = 0 
        break
print(f"the number showing on the list {counter} times")

n3 = int(input("enter a number to delete it from the list: "))
for i in lis:
    if i == n3:
        lis.remove(n3)
        #אופציה א
    elif n3 not in lis:
        print("the numer you pick is not on the list")
        break
    #אופציה ב 
    else:
        i+=1
print(lis)

n4 = int(input("enter a number to create a list that is bigger then this number: "))
lis2 =[]
lis2.append(n4)
for i in lis:
    if i > n4:
        lis2.append(i)
print(lis2)
