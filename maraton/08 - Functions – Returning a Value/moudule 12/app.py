import calculator_prime as c

print("==========TRY=========")
for i in range(3):
    returning_list =  []
    for j in range(3):
        n = int(input("entr number to know if he prime number: "))
        returning_list.append(n)
    x = c.some_list(returning_list)
    print(x)