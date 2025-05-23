def is_up(numbers):
    if len(numbers) == 0:
        raise ValueError ("list is empty! (in function)")
    for i in range(len(numbers)-1): #כי בתנאי בודקים שני אינדקסים ביחד אז כדי שזה לא יקפוץ לאינדקס אחד יותר אז מורידים אחד 
        '''
        זאת אומרת שאם יש לנו 4 מספרים זה 4 אינדקסים 
        אבל בתנאי אנחנו בודקים 2 ביחד מה שאומר שאנחנו צריכים לעבור על 3 אינדקסים 
        2,3 זה אחד
        3,4 זה שתיים 
        4,5 זה שלוש 
        סך הכל עברנו 3 אינדקסים  
        2,3,4,5 אבל זה 4 אינדקסים 
        בגלל זה בא המינוס אחד כדי שלא נקפוץ למספר שלא קיים ויחזיר שגיאה 

        '''
        if numbers[i+1] < numbers[i]: # אם המספר השני קטן מהמספר הראשון מתקיים ומחזיר שגיאה
            return False
    return True

num = is_up([2, 3, 4, 5])
print(num)