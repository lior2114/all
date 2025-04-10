while True:
    n = int(input("Enter a positive number (0 or negative to quit): "))
    if n <= 0:
        print("You are done")
        break
    for i in range(n):
        print(i+1, end="|")
    print() 
print ("Goodbye")