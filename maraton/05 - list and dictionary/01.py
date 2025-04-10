print("===========A===========")
car1 = {
    "manufacturer": "Toyota",
    "model": "Corolla",
    "year": 2020,
    "color": "Red"
}

car2 = {
    "manufacturer": "Honda",
    "model": "Civic",
    "year": 2019,
    "color": "Blue"
}

car3 = {
    "manufacturer": "Ford",
    "model": "Mustang",
    "year": 2021,
    "color": "Black"
}

print("===========B===========")
lis=[car1,car2,car3]
for cars in lis:
    for key,value in cars.items():
        print(f"{key}: {value}")
    print() 

print("===========C===========")
for v in lis:
    for key, value in v.items():
        print(value, end=" ")
    print()
