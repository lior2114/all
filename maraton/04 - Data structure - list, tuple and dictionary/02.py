tup = {"apple":10, "banana":20, "food":30, "melon":40, "goyava":50}
print(tup)
print()
print("============A=============")
for key, value in tup.items():
    if value == 10:
        print(key)

print("============B============")
for key in tup:
    print((key + " ") * 3)
print()

print("============C============")
counter = 0 
for words in tup.keys():
    for ch in words:
        counter +=1
print(f"sum of all characters in the words is: {counter}")

