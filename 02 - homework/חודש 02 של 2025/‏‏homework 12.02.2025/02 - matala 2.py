#א
products = ("apple", "banana", "peach", "headset", "table", "chair", "keyboard", "mouse", "monitor", "laptop")
print(products)
print()

#ב
print(products[0])
print()

#ג
for i in products:
    print((i + " ") * 3)
sum = 0 
for j in products:
    sum += len(j)
print(f"the sum of all the length on the list is: {sum}")
