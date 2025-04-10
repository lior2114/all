# אופציה א
for i in range(10):
    number = int(input("Enter number: "))
    for j in range (number):
        print(number *"*")
    print()

# אופציה ב
for i in range(10):
    number = int(input("Enter number: "))
    for j in range(number):
        for f in range(number):
            print("*",end = "")
        print() 