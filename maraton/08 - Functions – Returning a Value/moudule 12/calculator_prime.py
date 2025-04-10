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

