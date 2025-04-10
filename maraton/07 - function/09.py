import random
print("=======A========")
def li(lis):
    print(*lis, sep="|")

print("=======B========")
liss = [10,20,30,40]
li(liss)

print("=======C========")
liis = []
for i in range(4):
    n = random.randint(1,10)
    liis.append(n)
li(liis)