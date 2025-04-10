import random
lis = set()
print("============A=============")
for i in range (100):
    num = random.randint(1,1000)
    lis.add(num)
print(lis)
print(sum(lis)/len(lis))

print("============B=============")
num2 = int(input("enter number to know if he on the set: "))
if num2 in lis:
    print("yes he on the set")
else:
    print("No")

print("============C=============")
for i in lis:
    print(f"Number:{i}, Power:{i**2}")
    