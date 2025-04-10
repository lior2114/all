import class1 as clas
try:
    number1 = int(input("enter number1: "))
    number2 = int(input("enter number2: "))
    prime_numbers_file = clas.primes(number1,number2)
    listed = clas.list_call()
    print(listed)
    summ = 0
    for i in listed:
        summ += int(i)
    avg = summ /len(listed)
    print(avg)
except Exception as err:
    print(err)