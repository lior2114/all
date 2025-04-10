products = {3.5:"apple", 4:"Banana", 5:"peach"} #אם יש לנו שתי פריטים שהם אותו הדבר אז האחרון מבינהם דורס את הקודם
v = int(input("Enter a value: "))
p = input("Enter a product name: ")
# אופציה א
products[v] = p
print(products)

# אופציה ב
products.update({v:p})
print(products)

#חיפוש מילה למציאת מספר 
word =input("Enter a word to search for a price: ")
for i in products:
    if word == products[i]:
        print(i)
        break
    else:
        print("The word is not in the list")

#חיפוש מספר למציאת מילה
n1 = float(input("Enter a number to search for a product: "))
for j in products:
    if n1 == j:
        print(products[j])
        break
else:
    print("The number is not in the list")

    #  חיפוש מוצר לפי קוד מוצר אופציה ב
    code = float(input("Enter a product code to search for the product: "))
    if code in products:
        print(products[code])
    else:
        print("The product code is not in the list")

for i in products:
    print(f"Priduct ID: {i}, Product Name: {products[i]}")

n2 = float(input("Enter a number ID delete a product: "))
if n2 in products:
    products.pop(n2)
else:
    print("product ID not exist")
print(products)