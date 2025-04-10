import random
print("=======A========")
def som(x1):
    if x1 == 1:
        print(":-)")
    elif x1 == 2:
        print(":-(")
    elif x1 == 3:
        print(":-/") 
    elif x1 == 4:
        print(";-)")   
    elif x1 == 5:
        print(";-(") 

print("=======B========")
som(4)

print("=======C========")
n1 = int(input("enter number between 1-5 to print smilie: "))
som(n1)

print("=======D========")
n2 = random.randint(1,5)
som(n2)

print("=======E========")
def all():
    for i in range(5):
        som(i+1) #בגלל שהאיי מתחיל ב - 0 אז מוסיפים אחד כי באפס אין שום סמיילי
all()

print("=======F========")
def ran():
    for i in range(100):
        n3 = random.randint(1,5)
        som(n3)
ran()