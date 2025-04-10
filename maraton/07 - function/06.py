import random
print("=======A========")
def som(x1,x2,x3):
    if x1 > x2 and x1 > x1:
        print(x1)
    elif x2 > x1 and x2 > x3:
        print(x2)
    else:
        print(x3)

print("=======B========")
som(10,20,30)

print("=======C========")
n1 = int(input("enter number1: "))
n2 = int(input("enter number2: "))
n3 = int(input("enter number3: "))
som(n1,n2,n3)

print("=======D========")
b1 = random.randint(1,1000)
b2 = random.randint(1,1000)
b3 = random.randint(1,1000)
print(b1,b2,b3) #כדי לראות מה המספרים 
som(b1,b2,b3)