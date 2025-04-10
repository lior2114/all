import os
def bewtween_two_numbers (num1,num2):
    if num1>num2:
        num1,num2 = num2,num1
    folder_name = "two_number"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    with open (f"./{folder_name}/between_two_number.txt", 'w') as two_number_file:
        for i in range(num1,num2+1):
            two_number_file.write(f"{i} \n")
    lis = []
    with open (f"./{folder_name}/between_two_number.txt", 'r') as two_number_file:
        for line in two_number_file:
            lis.append(line.strip())
    summ = 0
    for n in lis:
        summ += int(n)
    avg = summ / len(lis)
    return lis, summ, avg
