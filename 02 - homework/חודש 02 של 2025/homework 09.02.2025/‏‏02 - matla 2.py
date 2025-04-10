names = []
for i in range (5):
    name = input(f"enter name {i}: ")
    names.append(name)
print(f"all names are: {names}")
print(f"the first name are {names[0]}, and the last name is:{names[-1]}")

counter = 0 
for x in names:
    counter += len(x)
    print(f"the letter in the lines are: {counter}")
    counter = 0

names.reverse()
print (f"the names in reverse are: {names}")