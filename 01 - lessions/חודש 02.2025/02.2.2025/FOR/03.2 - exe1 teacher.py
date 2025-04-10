print ("a need to be bigger than b")
a = int(input("enter number a (the starting number): "))
b = int(input("enter number b (the stopping number): "))
for i in range ( a, b+1):  #+1 כדי שיכליל גם את המסםר האחרון 
    if i%2 ==0:
        print (i, END = ", ")