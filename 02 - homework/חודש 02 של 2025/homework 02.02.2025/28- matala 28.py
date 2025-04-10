# קלטו מספר n
n = int(input("enter a number: "))

# הדפיסו את כל הכפולות של n עד 100
for i in range(1, 101):
    if n % i == 0:
        print(i)