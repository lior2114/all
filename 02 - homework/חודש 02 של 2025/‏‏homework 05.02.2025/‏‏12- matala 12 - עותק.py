counter = 10
for i in range (0, counter):
    n1 = int(input("enter a number1: "))
    n2 = int(input("enter a number2: "))
    while n1 > 0 or n2 > 0:
        if n1<n2:
            print(n2)
            break            
        elif n1 > n2:
            print (n1)                 
            break
    if n1 < 0 or n2 < 0:
        print ("enter a positive number ")
        counter = i 
        break
            
