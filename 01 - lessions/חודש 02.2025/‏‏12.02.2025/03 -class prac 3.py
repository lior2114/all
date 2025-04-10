items = set()
for i in range (1,6):
    mozar = input(f"enter the {i} mozar: ")
    items.add(mozar)
print (items)

mozar2 = input(f"enter the mozar 6: ")
items.add(mozar2)
for mozar in items:
    print (mozar, end = "|")
print()

print(f"the numbers of products is {len(items)}")