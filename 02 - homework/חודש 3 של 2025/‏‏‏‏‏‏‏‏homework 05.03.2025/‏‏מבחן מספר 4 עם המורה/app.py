import handle_str as st
import handle_digits as dig
import handle_test as te
try:
# 1 - handle_str
    word = 'aaaaa'
    the_result = st.in_same_charsv2(word)
    print(the_result)

# 2 - handle_digits
    digits = 12345 # true
    digits2 = 12845 # false כי יש שתי ספרות זוגיות אחת אחרי השניה 
    digits2 = 123455 # false כי יש שתי מספרים אי זוגיים אחד אחרי השני 
    if isinstance(digits,str):
        raise ValueError ("enter only numbers! (in app)")
    the_result_for_digits = dig.even_odd_even(digits)
    print(the_result_for_digits)

#3 - handle_test
    listed = []
    for i in range(100):
        listed.append(i)
    for i in listed:
        if isinstance(i,str):
            raise ValueError("enter only numbers! (in app handle test)")
    prime_plus_index = te.for_list(listed)
    print(prime_plus_index)
        


except ValueError as err:
    print(err)
except TypeError as err:
    print(err)
except Exception as err:
    print("some error")

