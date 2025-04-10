print("==========A=========")
def some_number(num):
    if num <= 1:
        return False
    for i in range (2,num):
        if num % i == 0:
            return False
    else:
        return True

print("==========B=========")
while True:
    n = int(input("entr number to know if he prime number: "))
    x = some_number(n)
    print(x)