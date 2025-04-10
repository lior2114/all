import plus as ma
import user_data as use
import two_number as bet
import Prime_between_numbers as pri
import tkinter as tk
from tkinter import messagebox

try:

# 1 - math_plus
    num1 = int(input("enter number1: "))
    num2 = int(input("enter number2: "))
    return_plus = ma.sum_of_two_numbers(num1,num2)


# 2 - user_data
    while True:
        name = input("enter your name: ")
        if name.isalpha():
            break
        else:
            name_root = tk.Tk()
            name_root.withdraw()
            name_root.attributes("-topmost", True)
            messagebox.showerror ("invalid name", "enter only str")
            name_root.destroy()
    while True:
        lastname = input("enter your last name: ")
        if lastname.isalpha():
            break
        else:
            root = tk.Tk()  # יצירת שורש של הודעה
            root.withdraw()  # מסתיר את החלון שממנו לקוח המשאב
            root.attributes("-topmost", True)  # מוודא שהחלון יוצג מעל כל החלונות שיש ברקע 
            messagebox.showerror("Invalid Input", "Please enter only letters.")  # הראשון זה שם החלון השני זה מה שיופיע בו
            root.destroy()  # סוגר אותו כדי שלא ימשיך לרוץ ברקע ויקח משאבים

    while True:
        email = input("enter your email: ")
        if isinstance(email, str):
            break
        else:
            email_root = tk.Tk()
            email_root.withdraw()
            email_root.attributes("-topmost",True)
            messagebox.showerror("invaild mail", "pleases try input your mail again")
            email_root.destroy()

    while True:
        phone = input("enter your phone number: ")
        if phone.isdigit():
            break
        else:
            phone_root = tk.Tk()
            phone_root.withdraw()
            phone_root.attributes("-topmost",True)
            messagebox.showerror("invaile phone number", "plese enter correct phone number")
            phone_root.destroy()

    userdate_file = use.data(name,lastname,email,phone)
    print(userdate_file)
    

#3 - between_numbers
    while True:
        number1 = (input("enter number1: "))
        number2 = (input("enter number2: "))
        if number1.isdigit() and number2.isdigit():
            break 
        else: 
            between_root = tk.Tk()
            between_root.withdraw()
            between_root.attributes("-topmost",True)
            messagebox.showerror("invaild input", "plese enter only numbers")
            between_root.destroy()

    between = bet.bewtween_two_numbers(number1,number2)
    lis,summ,avg = between
    print(f"your list is: {lis}")
    print(f"your sum is: {summ}, your avg is: {avg}")


#4 - Prime_between_numbers
    while True:
        n1 = input("enter number1: ")
        n2 = input("enter number2: ")
        if n1.isdigit() and n2.isdigit():
            break
        else: 
            prime_root = tk.Tk()
            prime_root.withdraw()
            prime_root.attributes("-topmost",True)
            messagebox.showerror("invaild input Prime","please enter right input")
            prime_root.destroy()

    prime_return = pri.prime_between_two_number(int(n1),int(n2))
    lis,lene = pri.retrun_list(prime_return)
    print(f"{lis}\nlength of the list is:{lene}")
    
except ValueError as err:
    print(err)
except TypeError as err:
    print(err)
except Exception as err:
    print("some error")
