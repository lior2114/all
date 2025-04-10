import random
listn = set()

for i in range (100):
    n = random.randint(1,1000)
    listn.add(n)
print (listn)
avg = sum(listn) / len(listn)
print("Average:", avg)

# ב 
n1 = int(input("Enter a number to check if it is in the list: "))
if n1 in listn:
    print("Yes")
else:
    print("No")

# ג
for i in listn:
    print(f"number: {i}, Power: {i**2}")
