import handle_nubmers as nu
import handle_same_digits as dig
import handle_list as li

try:
    #1 - handle_numbers
    num = int(input("enter number: "))
    sum_of_digits = nu.sum_digits(num)
    print(f"the sum of the digits is: {sum_of_digits}")

    # 2 - handle_same_digits
    num2 = int(input("enter unfollowing numbers: "))
    if_number_return_inhimself = dig.not_same_digits(num2) 
    print(if_number_return_inhimself)

    if if_number_return_inhimself: #True
        print("same numbers")
    else: #False
        print("not same numbers")


    # 3 - handle_list
    lis = [1, 2, 3]
    sum_and_avarage_list = li.avarage_and_sum(lis)
    print(sum_and_avarage_list)
    print(li.avarage_and_sum(lis)) #אופציה ב 


except ValueError as err:
    print(err) #זה ידפיס את הודאת השגיאה שבאפפ אם יש 
except TypeError as err:
    print(err)
except Exception as err:
    print("some error")

