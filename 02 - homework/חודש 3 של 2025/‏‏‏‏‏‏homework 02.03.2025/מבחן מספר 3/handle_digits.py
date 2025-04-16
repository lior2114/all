def count_even_odd_digit (n):
    new_n = str(n)  # בגלל שבאפפ משמש כמספר 
    split_counter = 0
    not_split_counter = 0 
    for i in new_n:
        if int(i) % 2 == 0: # כדי להמיר את המחרוזת למספר כדי לבדוק האם מתחלק ב 2
            split_counter+=1
        else:
            not_split_counter += 1
    tuples = (split_counter,not_split_counter)
    return tuples