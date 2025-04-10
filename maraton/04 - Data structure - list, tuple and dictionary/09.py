import random
lis = []
for i in range(20):
    num = random.randint(1, 10)
    lis.append(num)
print(lis)

lisnew = {}
for numbers in lis:
    if numbers in lisnew:
        lisnew[numbers] += 1
    else:
        lisnew[numbers] = 1

maxx = max(lisnew.values())

most = []
for key,value in lisnew.items():
    if value == maxx:
        most.append(key)
print(f"most return number is: {most}, and it returns {maxx} times")
print(most)

