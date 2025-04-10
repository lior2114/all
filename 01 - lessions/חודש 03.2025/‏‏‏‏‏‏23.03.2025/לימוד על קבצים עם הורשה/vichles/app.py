from vehicle import * # * זה הכל משם
try:
    c1 = Car("honda",4)
    b1 = Bicycle("buggati", True)
    a1= Airplane("lambo", 2)
    all_vehicles = [c1,b1,a1]

    for a in all_vehicles:
        a.move()
    if isinstance(b1,Bicycle):
        b1.hasbasket()
except Exception as err:
    print(err)