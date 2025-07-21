cat_name = "Fluffy"
cat_age = 3
cat_color = "Black"
cat_food = "Fish"

#שאלה 1 
cat1 = {"name": cat_name, "age": cat_age, "color": cat_color, "food": cat_food}
#אופציה א
print("=================1-A===================")
print(cat1["name"]) #Fluffy
print(cat1["age"]) #3
print(cat1["color"]) #Black 
print(cat1["food"]) #Fish   

print("==================1-B==================")
 #אופציה ב
for value in cat1:
    print(cat1[value])

print("==================2==================")
#שאלה 2
cat2 = {"name": "Misty", "age": 2, "color": "White", "food": "Milk"}
cat3 = {"name": "Whiskers", "age": 1, "color": "Gray", "food": "Meat"}
all_cats = [cat1, cat2, cat3]
for i in all_cats:
    print(i["name"])

#שאלה 3
print("==================3==================")
summ = 0 
for i in all_cats:
    summ += i["age"]
print(summ)

print("==================4==================")
for i in all_cats:
    print("===========================")
    print(f"Name: {i["name"]}")# האיי מייצג את השורה והשם בצד מייצג את מה שאנחנו רוצים להציג מתוך השורה הזו
    print(f"Age: {i["age"]}")
    print(f"Color: {i["color"]}")
    print(f"Food: {i["food"]}")
    print() #להדפיס רווח ריק בין כל חתול   
