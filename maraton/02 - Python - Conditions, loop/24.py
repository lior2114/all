number = int(input("enter nubmer: "))
#אופציה א
for i in range(number):
    for j in range (number):
        print("*",end ="")
    print()

#אופציה ב
for i in range(number):
    print(number*"*")