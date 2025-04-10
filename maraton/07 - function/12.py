print("=======A========")
def ran(length):
    for i in range(length):
        print("*", end =" ")
    print()

def siz(size):
    for i in range(size):
        ran(size)

print("=======B========")
siz(10)

print("=======C========")
number = int(input("enter number for square: "))
siz(number)

