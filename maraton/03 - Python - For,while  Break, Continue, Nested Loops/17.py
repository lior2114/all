n = int(input("enter number: "))
#אופציה א
print("======A======")
for i in range(n):
    for j in range(n):
        print("*", end ="")
    print()
print()

print("======B======")
#אופציה ב
for i in range(n):
    print(n*"*")