import random

def display_count_random(count):
    for i in range(count):
        num = random.randint(-50, 50)
        print(num)
display_count_random(10) #  קוראים לפונקציה שמדפיסה מספר רנדומלי וכל פעם שהיא נקראת היא מדפיסה מספר אחר עשר פעמים 
# כי משווים את הקאונט ל 10 