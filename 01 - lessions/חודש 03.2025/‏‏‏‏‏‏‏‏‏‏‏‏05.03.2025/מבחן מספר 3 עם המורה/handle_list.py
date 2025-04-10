def min_max(lis):
    if len(lis) <= 0:
        raise ValueError ("list is empty! (in min_max function)")
    maxx = 0 # אפשר גם maxx = lis[0]
    minn = float('inf') # אפשר גם minn = lis[0]
    for i in lis:
        new_i = str(i) # ממירים למחרוזת כדי שיהיה אפשר לרוץ על כל מה שרשום בה ולבדוק אם זה מספר או לא 
        if not new_i.isdigit():
            raise TypeError ("enter only numbers! (loop i in function)")
        if i > maxx:
            maxx = i 
        if i < minn:
            minn = i
    tuples = (minn,maxx)
    return tuples


def min_max2(listed):
    if len(listed) <= 0:
        raise ValueError ("list is empty! (in min_max function)")
    '''
    לשים לב לסוגרים בריטרן כל אחד מחזיר אותו באופן שונה
    '''
    return min(listed),max(listed) #ככה זה מחזיר טופל בלי סוגרים בסוף ובהתחלה 
    return [min(listed),max(listed)] #ככה זה מחזיר ליסט
    return {min(listed),max(listed)} #ככה זה מחזיר סט