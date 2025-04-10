import random
numbers = []
for i in range (10):
    num = random.randint(0,100) 
    numbers.append(num)

print(numbers)
print()

numbers.reverse()
print (numbers)

s = sum(numbers)
print(s)
print()

avg = s/len(numbers)
print(avg)
print()

for sp in numbers:
    if sp%2==0:
        print(f"the numbers that are splits in 2 are: {sp}")
        print()

for unsp in numbers:
    if unsp %2 ==1:
        print(f" dont split are: {unsp}")
        print()

counter7=0
for sp7 in numbers:
    if sp7%7==0:
        counter7+=1
print(f"there are {counter7} numbers that split in 7")

maxnum = numbers[0]
for i in numbers:
    if i > maxnum:
        maxnum = i 
print(f"the max number in the list is: {maxnum}")

minnum = numbers[0]
for j in numbers:
    if j < minnum:
        minnum = j
print(f"the mini number in the list is: {minnum}")


print(f"avg is {avg}")
for num in numbers:
    if num > avg or num == avg:
        print(f"the numbers that are bigger or Equal to the avarage is: {num}")
