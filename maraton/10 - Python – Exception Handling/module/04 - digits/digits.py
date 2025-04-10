def n_and_digit(n,digit):
    counter = 0 
    n_new = str(n)# הפיכה למחרוזת כדי שנוכל לבדוק את המספרים שבתוכה
    digit_new = str(digit) # הפיכה למחרוזת כדי שנוכל לבדוק את ההופעה שלו בתוך מה שהפכנו למחרוזת 
    for i in n_new:
        if digit_new == i:
            counter += 1
        #digit   כדי שיחזיר מספר ולא מחרוזת כדי שנוכל להשתמש בו במידת הצורך
    return counter,digit