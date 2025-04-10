lis = {100:"comcom", 200:"spoon", 300:"fork"}

print("============A=============")
name = input("add name of the product: ")
number = int(input("enter product ID: "))
lis.update({number:name})
print(lis)

print("============B=============")
num = int(input("enter ID to search a product: "))
if num in lis:
    print(lis[num])
else:
    print("no")

print("============C=============")
for key,value in lis.items():
    print(f"Product ID: {key}, Product Name: {value}")


print("============D=============")
num2 = int(input("enter Product ID to delete it: "))
if num2 in lis:
    lis.pop(num2)
    print(lis)
else:
    print("Product ID not exist")
#אם הקוד לא קיים הוא ממשיך כרגיל ורושם הקוד לא קיים