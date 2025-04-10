import random 

random_num = random.randint(1,100)
for i in range (random_num):
    guess = int(input("enter a number: "))
    if guess == random_num:
        print ("you win!")
    elif guess < random_num:
        print ("too low")
    elif guess > random_num:
        print ("too high")    
    elif guess != random_num or guess == ValueError: 
        print ("try again")
        i += 1 