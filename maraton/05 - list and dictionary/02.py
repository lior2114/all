print("===========A===========")
clothes = [
    {"type": "shirt", "size": "M", "price": 20, "color": "blue"},
    {"type": "pants", "size": "L", "price": 35, "color": "black"},
    {"type": "jacket", "size": "S", "price": 50, "color": "green"},
    {"type": "dress", "size": "M", "price": 45, "color": "red"},
    {"type": "skirt", "size": "XS", "price": 25, "color": "yellow"}
]

print("===========B===========")
for i in clothes:
    for key,value in i.items():
        print(value, end =" ")
    print()

print("===========C===========")
summ = 0 
counter = 0
for items in clothes:
    summ += items["price"]
    counter += 1
print(summ/counter)

print("===========D===========")
maxprice = 0
for i in clothes:
    if i["price"] > maxprice:
        maxprice = i["price"]
print(maxprice)
