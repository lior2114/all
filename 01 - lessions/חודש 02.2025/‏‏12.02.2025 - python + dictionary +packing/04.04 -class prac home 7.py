import random

# #אופציה א'
numbers = set()
while len(numbers)<6:
    num = random.randint (1,37)
    numbers.add(num)
print(numbers)
 
 #אופציה ב'
while True:
    num = random.randint (1,37)
    numbers.add(num)
    if len(numbers) ==6:
        break
print(numbers)