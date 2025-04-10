for j in range (5):
    counter = 1 
    n = int(input("enter a number:"))
    for i in range (0,n):
        if n%10 == 0:
            counter += 1
            n = n//10
    print (counter)