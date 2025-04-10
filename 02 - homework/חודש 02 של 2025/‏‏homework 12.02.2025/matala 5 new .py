import random
se = set()

for i in range (1000000):
    n = int(random.randint(1,100))
    se.add(n)
print(se)
print(sum(se))
#זה מראה דווקא את הסכום 5050 כי לא יכולים להיות כפילויות בסט אז הוא מוחק את מה שבכפילות