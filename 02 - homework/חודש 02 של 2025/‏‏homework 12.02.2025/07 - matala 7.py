import random

ran = set()
for i in range(14):
    for j in range(6):
        n = random.randint(1,37)
        ran.add(n)
        if len(ran) == 6:
            print(ran)
            ran.clear()