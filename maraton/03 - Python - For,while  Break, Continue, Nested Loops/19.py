n = int(input("enter number: "))

#אופציה א 
for i in range(n):
    for j in range(n):
        print("*",end ="")
    n -= 1
    print(i,n)
    print()

#אופציה ב
for i in range(1,n+1):
    print(n*"*",end = "")
    n -=1 
    print()