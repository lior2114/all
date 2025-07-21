import os

while True:
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print("The number is even.")
        exit_input = input("write 'exit' to exit ")
        if exit_input == 'exit':
            break
    os.system('cls' if os.name == 'nt' else 'clear')
    