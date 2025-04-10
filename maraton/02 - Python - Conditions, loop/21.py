x = 1 
summ2 = 0
counter = 0 
while x > 0 or x == 0:
    number = int(input("enter a number: "))
    x = number
    if number == 0:
        continue
    if number%2== 0:
        summ2+=number
        counter += 1
print(f"summ of the split 2 number is {summ2} and there was {counter} numbers that split in 2")