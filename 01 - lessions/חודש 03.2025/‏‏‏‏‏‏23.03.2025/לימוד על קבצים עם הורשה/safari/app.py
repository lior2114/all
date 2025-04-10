from Animals import *
try:
    l1 = Lion ("lion1", "meet")
    e1 = Elephant("Elephant1", "pilpel", 10)
    m1 = Monkey("monkey","bananas",50)
    animals = [l1,e1,m1]
    for a in animals:
        print(a, end = '|')
        a.make_sound()
    
    print("=========")
    powers = 0
    for a in animals:
        if isinstance (a,Monkey):
            powers+=a.power()
    print(powers)
        # powers += a.power # מנסה לגשת לפונצקיה שאין לכולם אז יקרוס לכן נעשה: 
except Exception as err: 
    print(err)