print("==========A=========")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def some_list(listed):
    for number in listed:
        if not is_prime(number):
            return False
    return  True

print("==========B=========")
for i in range(3):
    returning_list =  []
    for j in range(3):
        n = int(input("entr number to know if he prime number: "))
        returning_list.append(n)
    x = some_list(returning_list)
    print(x)