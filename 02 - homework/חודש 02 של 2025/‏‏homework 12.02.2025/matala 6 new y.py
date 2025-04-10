products = {3:'apple', 4:'banana', 5:'peach'}

n = int(input("enter a product ID: "))
name = input("enter the name of the product: ")
products.update({n:name})
print(products)

n2 = int(input("serach for the product enter product ID : "))
for i in products:
    if n2 == i:
        print(products[i])
        break
    elif n2 not in products:
        print("product ID not exist")
        break

for i in products:
    print(f"Product ID: {i}, Product name: {products[i]}")

n3 = int(input("enter product ID to delte it from the list: "))
if n3 in products:
    products.pop(n3)
elif n3 not in products:
    print("the ID not exist")
print(products)
