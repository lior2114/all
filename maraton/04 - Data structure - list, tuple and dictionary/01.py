import random
print("=========A========")
List = []
for i in range(10):
    num = random.randint(1,10)
    List.append(num)
print(List)
print()
print(f"the length of the list is: {len(List)}")

print("=========B========")
num2 = int(input("enter a number to know if he on the list: "))
if num2 in List:
    print("yes")
else:
    print("no")


print("=========C========")
num3 = int(input("enter a number to know how many times he on the list: "))
counter = 0 
for i in List:
    if i == num3:
        counter+=1
    else:
        i+=1
print(f"number was showing {counter} times")


print("=========D========")
num4 = int(input("enter number to delete from the list: "))
new_list=[]
for i in List:
    if i == num4:
        i+=1
    else:
        new_list.append(i)
print(new_list)

print("=========E========")
num5 = int(input("enter number to add the numbers above him to a new list: "))
list_new = []
for i in List:
    if i > num5:
        list_new.append(i)
    else:
        i+=1
print(list_new)