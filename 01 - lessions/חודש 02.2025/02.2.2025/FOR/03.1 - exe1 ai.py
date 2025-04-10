print ("a need to be bigger than b")
a = int(input("enter number a (the starting number): "))
b = int(input("enter number b (the stopping number): "))
if a < b:
    print("a needs to be bigger than b")
else:
    for i in range(a, b, 2): # start = 10; stop = 100 jump = 2 
        print(i, end=", ")