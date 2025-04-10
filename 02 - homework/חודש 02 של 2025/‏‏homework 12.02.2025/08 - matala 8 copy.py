s = input("Enter a sentence: ")
d = {}
for char in s:
    if char in d:
        d[char] +=1
    else:
        d[char] = 1
common = max(d, key = d.get)
print(f"the most common character is {common} which appears {d[common]} times")
