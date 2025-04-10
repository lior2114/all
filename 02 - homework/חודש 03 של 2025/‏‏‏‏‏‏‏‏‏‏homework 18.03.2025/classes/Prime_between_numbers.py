import os
def prime_between_two_number (num1,num2):
    if num1>num2:
        num1,num2 = num2,num1
    folder_name= "prime_bewtween_two_numbers"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open(f"{folder_name}/primes.txt",'w') as prime_between_two_numbers:
        for i in range(num1,num2):
            its_prime = True
            for j in range(2,i):
                if i%j == 0:
                    its_prime = False
                    break
            if its_prime:
                prime_between_two_numbers.write(f"{i}\n")
    return folder_name

def retrun_list(folder_name):
    with open(f"{folder_name}/primes.txt", 'r') as prime_between_two_numbers:
        lis = []
        for line in prime_between_two_numbers:
            lis.append(line.strip())
    lene = len(lis)
    return lis, lene
