# לא הכי מובן 
def divide_until_one(number):
    count = 0
    while number > 1:
        number /= 2
        count += 1
    return count

# Example usage
number = int(input("Enter a number: "))
print(f"The number was divided {divide_until_one(number)} times until it reached 1.")
