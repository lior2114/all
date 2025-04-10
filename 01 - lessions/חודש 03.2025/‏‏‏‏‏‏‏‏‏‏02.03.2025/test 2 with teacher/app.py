import handle_words as han
import handle_digits as dig
import handle_list as li
import handle_matrix as mat
import random
try:
    print("=======A=======")
    name1 = input("enter name1: ")
    char = input("enter char: ")
    truefalse = han.handle_words(name1,char)
    print(truefalse)

    print("=======B=======")
    ifin_x2 = dig.exist_digits(10,9)# יעשה לי אירור כי יש אות 
    print(ifin_x2)

    print("=======C=======")
    listed1 = [1,2,3,'r'] #אם נשים אותו זה ידפיס שגיאה כי יש אות 
    listed = [1,2,3,3] 
    number = 3
    remove_num_from_list = li.remove_number(listed,number)
    print(remove_num_from_list)
    # # print("=======C2=======") #אם אין ריטרן אז ככה  עושים
    # # listed = [1,2,3,3] #ידפיס שגיאה כי יש אות 
    # # number = 3
    # # li.remove_number2(listed,number)#עושה את הפעולה של המחיקה 
    # # print(listed) #מחזירים את הרשימה כי הפונקציה כבר מחקה ממנה את מה שאנחנו רצינו למחוק 

    print("=======D=======")
    matriza = [
            [100,20,30],        
            [40,50,60],
            [70,80,90]
    ]
    max_number_in_rows = mat.max_number_and_index(matriza)
    print(max_number_in_rows)
    max_value,row,col = mat.max_number_and_index(matriza) #בגלל שהוא מחזיר לנו 3 משתנים אז משווים אותו אליהם ואז אפשר להציג אותם 
    print(f"max:{max_value}, max row: {row}, max col: {col}")

except ValueError as err:
    print(err)
except TypeError as err:
    print(err)
except Exception as err: #תקלות בכללי 
    print(err)
