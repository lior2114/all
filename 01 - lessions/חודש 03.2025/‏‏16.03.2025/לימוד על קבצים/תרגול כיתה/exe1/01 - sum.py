
try:
    x = int(input("enter number 1: "))
    y = int(input("enter number 2: "))
    soulution = x+y
    with open("./exe1/plus.txt", 'w') as file:
        file.write(f"{x} + {y} = {soulution}")
        
except Exception as err:
    print(err)
