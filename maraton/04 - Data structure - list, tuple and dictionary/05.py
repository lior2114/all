import random
lis = set()
print("============A=============")
for i in range (1000000):
    num = random.randint(1,100)
    lis.add(num)
print(sum(lis))
#הסכום שיוצא הוא 5050 כי בסט יכול להיות רק מספר אחד תואם