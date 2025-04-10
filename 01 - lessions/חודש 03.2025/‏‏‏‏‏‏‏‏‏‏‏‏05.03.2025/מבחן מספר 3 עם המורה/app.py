import handle_str as st
import handle_digits as dig
import handle_list as li
import handle_dict as di
try:
# 1 - handle_str
    word = input("enter word: ")
    if word.isdigit():
        raise ValueError ("enter a-z or A-Z! (word in app)")
    ch = input("enter character a-z or A-Z: ")
    if ch.isdigit():
        raise ValueError ("enter a-z or A-Z! (ch in app)")
    counter = st.count_chr(word,ch)
    print(f"the character {ch}, appears in {word}, {counter} times")

# 2 - handle_digits
    n = input("enter numbers: ")
    if not n.isdigit():
        raise ValueError ("enter only numbers! (n in app)")
    new_n = int(n) #  לא חובה רק כדי שישמש כמספר אם צריך בהמשך לדוגמא כמו 
                   # שאם הוא יהיה 0 שיהיה אפשר לקלוט אותו ולהציף את הבעיה כמו בשורה הבאה
    if new_n == 0:
        raise ValueError ("enter numbers! (new_n in app)")
    tuples_of_split_ornot_counter = dig.count_even_odd_digit(new_n)
    print(tuples_of_split_ornot_counter)

# # 3 - handle_list
    lis = [10,20,'y',22,23,24,30] #בגלל שיש כאן אות זה יעצור ויציף את הודעת השגיאה שבתוך הפונקציה
    minmax = li.min_max(lis)
    print(minmax)

# 4 - handle_dict
    dict = {'apple':500,'banana': 600, 'peach':100}
    max_in_tuple_return = di.max_product_price(dict)
    print(max_in_tuple_return)
    
except ValueError as err:
    print(err)
except TypeError as err:
    print(err)
except Exception as err:
    print("some error")

