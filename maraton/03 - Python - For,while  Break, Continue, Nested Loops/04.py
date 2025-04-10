x = 1 
while x >= 0: 
    num = int(input("enter number or -number to stop: "))
    x = num
    if num == 0:
        print("0 is not negative or true number") 
    elif num > 0: 
        print(f"the number is true and its **3 is: {num**3}")
    elif num < 0:
        break