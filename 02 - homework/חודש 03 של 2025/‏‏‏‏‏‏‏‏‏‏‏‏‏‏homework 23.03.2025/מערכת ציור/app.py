from painting import *
try:
    c1 = Circle("red", 180)
    s1 = Square("yellow", 100)
    t1 = Triangle("pink", 8, 10)
    all = [c1,s1,t1]
    for a in all:
        a.draw()
        if isinstance (a,Triangle):
            print(a.triangle_area())
except ValueError as err:
    print(err)
except Exception as err:
    print(err)