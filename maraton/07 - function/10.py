import random 
print("=======A========")
def li(lis):
    summ = 0 
    for i in lis:
        summ += i 
    print(summ/len(lis))

print("=======B========")
listed  = [10,20,30,40]
li(listed)

print("=======C========")
listed = []
for i in range(4):
    n = random.randint(1,20)
    listed.append(n)
print(listed)
li(listed)