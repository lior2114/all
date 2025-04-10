def count_even_odd_digit (n):
    new_n = str(n)  # בגלל שבאפפ משמש כמספר 
    split_counter = 0 #even
    not_split_counter = 0 #odd
    for i in new_n:
        if int(i) % 2 == 0: # כדי להמיר את המחרוזת למספר כדי לבדוק האם מתחלק ב 2
            split_counter+=1
        else:
            not_split_counter += 1
    tuples = (split_counter,not_split_counter)
    return tuples

def count_even_odd_digitv2 (num):
    even = 0
    odd = 0 
    while num != 0:
        if (num%10)%2 == 0: 
            even += 1
        else:
            odd +=1 
        num = num//10 #delete last digit 
    return even,odd #מחזיר טופל

#אופציה א
x = 222333
t = count_even_odd_digitv2 (x)
print(f"{x} has {t[0]} even numbers and {t[1]} of odd numbers")

# אופציה ב 
x = 222333
e,o = count_even_odd_digitv2(x)
print(f"{x} has {e} even numbers and {o} of odd numbers")