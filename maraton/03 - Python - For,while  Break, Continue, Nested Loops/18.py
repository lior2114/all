length = int(input("enter length: "))
high = int(input("enter high: "))
#אופציה א
print("======A======")
for i in range(high):
    for j in range(length):
        print("*", end ="")
    print()
print()

print("======B======")
#אופציה ב
for i in range(high):
    print(length*"*")