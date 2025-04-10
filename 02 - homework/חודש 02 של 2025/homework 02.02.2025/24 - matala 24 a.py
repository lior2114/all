
count = 0

while True:
    number = int(input("Enter a number: "))
    if number < 0:
        break
    count += 1

print("Total numbers entered (excluding the negative number):", count)