import handle_str as st
import handle_digits as dig
try:
# 1 - handle_str
    word = 'aaaaa'
    the_result = st.in_same_charsv2(word)
    print(the_result)

# 2 - handle_digits
    digits = 12345
    if isinstance(digits,str):
        raise ValueError ("enter only numbers! (in app)")
    the_result_for_digits = dig.even_odd_even(digits)
    print(the_result_for_digits)


except ValueError as err:
    print(err)
except TypeError as err:
    print(err)
except Exception as err:
    print("some error")

