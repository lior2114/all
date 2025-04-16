def max_product_price(dict):
    if len(dict) == 0:
        raise ValueError ("dictionary is empty! (in fucnction at the start)")
    maxx = 0
    max_word = ' '
    for key,value in dict.items(): #אפילו שזה לא פועל האייטמס אם מכניסים דיקשינרי שזה מילון אז זה יעבוד 
        if value > maxx:
            maxx = value
            max_word = key
    tup = (max_word,maxx)
    return tup 