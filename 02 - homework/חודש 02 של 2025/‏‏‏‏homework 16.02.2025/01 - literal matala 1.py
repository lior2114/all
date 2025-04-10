

car1 = {"creator": "tony", "model": "Toyota", "year": 2020, "paint": "black"}
car2 = {"creator": "alice", "model": "Honda", "year": 2018, "paint": "white"}
car3 = {"creator": "bob", "model": "Ford", "year": 2022, "paint": "blue"}
cars = [car1, car2, car3]

print("=======A=======")
for car in cars:
    print(f"Creator: {car['creator']}")
    print(f"Model: {car['model']}")
    print(f"Year: {car['year']}")
    print(f"Paint: {car['paint']}")
    print("-------------")

print("=======B=======")
for car in cars:
    for key, value in car.items(): #עושה פרינט לכל המפתחות והערכים של הרכב מתוך המילון
        print(f"Car {key}: {value}")
    print("-------------")

