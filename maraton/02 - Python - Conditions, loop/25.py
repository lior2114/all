rohav = int(input("enter rohav: "))
length = int(input("enter length: "))

for i in range (length):
    for j in range(rohav):
        print("*", end ="")
    print()
    
print()
for i in range(length):
    print(rohav * "*")