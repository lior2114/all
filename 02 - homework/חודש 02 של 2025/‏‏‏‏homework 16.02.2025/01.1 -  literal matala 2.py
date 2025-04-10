print("========A=========")
cloth1 = {"type": "shirt", "size": "M", "price":20, "color": "blue"}
cloth2 = {"type": "pants", "size": "L", "price":30, "color": "black"}
cloth3 = {"type": "jacket", "size": "S", "price":40, "color": "white"}
cloth4 = {"type": "hat", "size": "XL", "price":10, "color": "red"}
cloth5 = {"type": "socks", "size": "S", "price":5, "color": "green"}
all_clothes = [cloth1, cloth2, cloth3, cloth4, cloth5]

print("========B=========")
for cloth in all_clothes:
    for key, value in cloth.items():
        print(f"the mafyen of the {key} is: {value}")
    print("----")

print("========C=========")
summ = 0
counter = 0  
for i in all_clothes:
    summ += i["price"]
    counter += 1 
print(summ)
print(int(summ/counter))

print("========D=========")
max = 0
for i in all_clothes:
    for j in i:
        if j == "price":
            if i[j] > max:
                max = i [j]
print(max)