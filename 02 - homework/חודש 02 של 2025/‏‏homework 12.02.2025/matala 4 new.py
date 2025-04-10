import random
se = set()
for i in range (100):
    n = int(random.randint(1,1000))
    se.add(n)
print(se)
print(sum(se)/len(se))

n2 = int(input("enter a number to check if he on the list: "))
if n2 in se:
    print("yes")
elif n2 not in se:
    print("no")

for i in se:
    print(f"Number: {i}, Power: {i**2}")