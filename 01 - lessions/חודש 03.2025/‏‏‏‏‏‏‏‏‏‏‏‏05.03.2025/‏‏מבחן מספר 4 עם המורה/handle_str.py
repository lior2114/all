def in_same_chars(word):
    new_word = str(word)
    if not isinstance(word,str):
        raise ValueError("enter only words! (in function)")
    if not word.isalpha():
        raise ValueError ("word has to be a-z, A-Z") #לגבי פסיקים ונקודות
    first_char = new_word[0] #לוקחים את המילה הרשונה במחרוזת ומכניסים למשתנה 
    for char in new_word:
        if char != first_char: 
            return False
    return True


def in_same_charsv2(word):
    word = set(word) #הסיר את כל האלה שמופיעים פעמיים 
    return(len(word)==1) #ואם אחרי ההסרה נשאר רק מספר אחד זה אומר שכולם היו שווים אז מחזיר אמת 