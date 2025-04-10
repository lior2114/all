import os
def sum_of_two_numbers(num1,num2):
    if not isinstance(num1,int) or not isinstance(num2,int):
        raise ValueError ("enter only numbers")
    folder_name = 'plus'
    if not os.path.exists (folder_name):
        os.makedirs(folder_name)
    with open(f"./{folder_name}/plus.txt", "w") as file:
        file.write(f"{num1}+{num2} = {num1+num2}" "\n")
 