x = 1
while x > 0: 
    number = int(input("enter number 0 to exit: "))
    x = number
    for i in range (number):
        for j in range(number):
            print(j+1 , end = ",")
        print()