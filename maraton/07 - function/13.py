import random
print("=======A========")
def stars(star):
    #אופציה א
    print(star*("*"))
    #אופציה ב
    # for i in range(star):
    #     print("*",end=" ")
    # print()

def hw(high,width):
    for i in range(high):
        stars(width)

print("=======B========")
hw(4,4)

print("=======C========")
high = random.randint(1,10) #אפשר לקרוא לערך איך שרוצים
width = random.randint(1,10) #אפשר לקרוא לערך איך שרוצים
hw(high,width)

print("=======D========")
high = int(input("enter high: ")) #אפשר לקרוא לערך איך שרוצים
width = int(input("enter width: ")) #אפשר לקרוא לערך איך שרוצים
hw(high,width)