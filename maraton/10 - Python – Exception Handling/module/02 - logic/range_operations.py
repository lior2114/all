import random
def generate_list(size,minn,maxx):
    if size == 0:
        raise ValueError ("enter size above 0! (size in function)")
    if minn > maxx: #בשאלה אומרים לעלות חריגה אם הוא יותר גדול אבל אפשר גם להפוך את זה ככה כדי שימשיך 
        minn,maxx = maxx,minn 
    lis = []
    for i in range(size):
        n = random.randint(minn,maxx)
        lis.append(n)
    return lis
