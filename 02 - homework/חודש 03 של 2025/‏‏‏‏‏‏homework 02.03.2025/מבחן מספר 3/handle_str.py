def count_chr (word,ch):
    counter = 0
    for chars in word:
        if ch == chars:
            counter += 1
    return counter 