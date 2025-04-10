counter = int(input("enter how much Number pairs you want to enter: "))
for i in range (counter):
        n1 = int(input("Enter number1: "))
        n2 = int(input("Enter number2: "))
        for n1 in range (n1,n2+1,1):
            print(n1, end="|")
        print()
        i +=1