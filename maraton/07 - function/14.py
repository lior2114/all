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
def c(count):
    for i in range(count):
        print(f"========{i+1}========")
        high = random.randint(2, 10)
        width = random.randint(1, 10)
        hw(high, width)

counter = int(input("Enter the number of times the rectangle will show: "))
c(counter)
