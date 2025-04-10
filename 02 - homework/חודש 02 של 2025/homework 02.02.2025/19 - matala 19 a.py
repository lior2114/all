import random
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

random_numbers = [random.randint(1, 100) for mashorandom in range(10)]
prime_numbers = [num for num in random_numbers if is_prime(num)]

print("Random numbers:", random_numbers)
print("Prime numbers:", prime_numbers)

