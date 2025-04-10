
for i in range (10):
    n1 = int(input("Enter number1: "))
    n2 = int(input("Enter number2: "))
    while n1 or n2 > 0:
        if n1 >= n2: 
            print (n1, end="|")
            print()
            break
        elif n1 <= n2:
            print (n2, end =  "|")
            print()
            break
    else:
        print ("you must enter a numer bigger than 0")
        i = 10
        break 
        