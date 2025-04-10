import os

def primes(number1, number2):
    if number1 > number2:
        number1, number2 = number2, number1  # החלפה אם הסדר לא נכון

    folder_name = "data"
    file_path = os.path.join(folder_name, "primes.txt")

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    try:
        with open(file_path, 'w') as file:
            for i in range(number1, number2 + 1):
                if i > 1:  # מספרים קטנים מ-2 אינם ראשוניים
                    is_prime = True
                    for j in range(2, i):
                        if i % j == 0:
                            is_prime = False
                            break
                    if is_prime:  # אם המספר ראשוני, כתוב לקובץ
                        file.write(f"{i}\n")

    except Exception as err:
        print(err)
            

def list_call():
    listed = []
    with open("./data/primes.txt", 'r') as file:
        for line in file:
            listed.append(line.strip())
    return listed

# primes(10, 100)
# print(list_call())