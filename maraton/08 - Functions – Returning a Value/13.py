import random
print("==========A=========")
def random_number(min,max):
    if min > max:
        min,max = max,min # יתחיל ממקסם כי קבענו שהמינימום הוא הנמוך אז עשינו סוויץ 
    n = random.randint(min,max)
    return n
print("==========B=========")
for i in range(3):
    min_number = int(input("enter min number: "))
    max_number = int(input("enter max number: "))
    x = random_number(min_number,max_number)
    print(x)