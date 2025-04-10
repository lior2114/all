number = int(input("Enter number: "))

if number <=1:
    prime = False
else:
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break

if prime:
    print("its prime")
else:
    print("its not prime")