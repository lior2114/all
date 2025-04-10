while True:
    n1 = int(input("Enter number1: "))
    n2 = int(input("Enter number2: "))
    if n1 > n2:
        for n2 in range (n2,n1+1):
            print(n2, end="|")       
            print() 
    elif n1 < n2:
        for n1 in range (n1,n2+1):
            print(n1, end="|")
            print()