x = int(input("enter number:"))
if x > 0:
    for i in range(x):
        print(i+1)
    print("backwards")
    for i in range (x,0,-1):
        print(i)