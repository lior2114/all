import random
print("=======A========")
def ran(start,end):
    n = random.randint(start,end)
    print(n)

print("=======B========")
ran(10,20)

print("=======C========")
n1 = int(input("enter number1: "))
n2 = int(input("enter number2: "))
ran(n1,n2)

print("=======D========")
for i in range(100):
    s = -10
    e = 10
    ran(s,e)