import list_cals as cal
try:
    size_input = input("enter size of list: ") # מתחילים ממחרוזת
    if not size_input.isdigit(): # אם המחרוזת היא לא מספר
        raise TypeError("enter only numbers! (size)") # אז מדפיסים בעיה
    size_input = int(size_input) # אם היא מספר אז ממירים אותה ל int ומכניסים לתוך משתנה חדש 
    
    lis = []
    for i in range(size_input):
        n = input("enter number for list: ") # אותו דבר כאן מתחילים ממחרוזת 
        if not n.isdigit():
            raise TypeError("enter only numbers! (num)")
        new_n = int(n) # המרה למספר לתוך משתנה חדש כדי שנוכל להוסיף אותו לליסט
        lis.append(new_n)
    avarage_list = cal.get_average(lis)
    print(avarage_list)

except ValueError as err:
    print(err)
except TypeError as err:
    print(err)
except Exception as err:
    print("some error")