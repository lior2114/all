print("=======A=======")
def handle_words(name1, char):
    #if (char < 'a' or char > 'z') or (char <'A' or char > 'Z'):
    if not char.isalpha() or not name1.isalpha(): #isdigit() רק למספרים וכאן זה אם זה לא אותיות
        raise ValueError("please enter a char a-z or A-Z")
    for chars in name1:
        if chars == char:
            return True
    return False
'''
if ch in word 
    return True
return False
'''