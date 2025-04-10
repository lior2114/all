print("========Max Numbers========")

#אופציה א'
def number(x,y,z):
    if x >= y and x >= z:
        print(x)
    elif y >= x and y >= z:
        print(y)
    else:
        print(z) # אפשרי גם לעשות ריטרן   
#מציג את המספר הגבוה כאשר אנחנו קובעים איזה מספרים יהיה ולא היוסר
number(1,2,3)

#אופציה ב'
def number2(x,y,z):
    for i in x,y,z:
        if i == max(x,y,z):
            print(i)

#אופציה ג'
def numbers3(x,y,z):
    arr = [x,y,z]
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    print(max)

#אופציה ד'
def numbers4(x,y,z):
    return max(x,y,z)

x1 = int(input("Enter number1: "))
x2 = int(input("Enter number2: "))
x3 = int(input("Enter number3: "))
number(x1,x2,x3)
number2(x1,x2,x3)
numbers3(x1,x2,x3)