tup = ( 'food', 'burger', 'fds')
print(tup)
print(tup[0])
all = 0 
for i in tup:
    all += (len(i))
    print((i + " ") * 3)

print(f"the length of all the words togher is: {all}")
