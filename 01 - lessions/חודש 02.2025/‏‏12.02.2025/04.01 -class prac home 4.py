products = {"black":"table", "orange":"paper", "white": "wall"}
print(products)
print(products["black"])
paint = input("enter a paint: ")
parit = input("enter a parit: ")

#הוספת פריט עם ערך לרשימה
products[paint] = parit
print(products)
products.update({paint:parit})
print(products)

for key in products:
    #           הפרודקט במקום הקי שזה המקום השני
    print(f"the color of {products[key]} is {key}")