import digits as di

try:
    n = input("enter numbers: ")
    if not n.isdigit():
        raise ValueError ("enter only numbers! (n)")
    new_n = int(n)

    digit = input("enter a digit: ")
    if not digit.isdigit():
        raise ValueError ("enter only numbers! (digit)")
    new_digit = int(digit)
    '''
    משווים שתי משתנים כי הפונקציה מחזירה שתי משתנים 
    אז כדי לקלוט אותם כאן משווים בסדר של הפונקציה כי ככה נדע מה מייצג מה\
    ואז אפשר להדפיס אותם כאן 
    אז
    counter = counter 
    number = digit 
    '''
    counter, number = di.n_and_digit(new_n,new_digit)
    print(f"number {number} is showing {counter} ")

except ValueError as err:
    print(err)
except TypeError as err:
    print(err)
except Exception as err:
    print("some eror")
