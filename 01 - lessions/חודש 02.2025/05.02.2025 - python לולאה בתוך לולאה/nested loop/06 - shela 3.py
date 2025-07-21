
#בודק האם המספר הוא מספר פריים אפשר להכניס עד 300 מספרים 
for i in range (300):
    n = int (input ("enter a number "))
    its_prime = True 
    for i in range (2, n):
        if n % i == 0:
            its_prime == False
            print (f"the number {n} its not a prime number")
            break
        print()
        if its_prime:
                 print (f"the number {n} its a prime number")
                 break

                 