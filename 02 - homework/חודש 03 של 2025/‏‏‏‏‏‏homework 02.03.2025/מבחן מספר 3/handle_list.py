def min_max(lis):
    if len(lis) <= 0 or len(lis) == 1:
        raise ValueError ("list is empty! (in min_max function)")
    maxx = 0 
    minn = float('inf')
    for i in lis:
        new_i = str(i)
        if not new_i.isdigit():
            raise TypeError ("enter only numbers! (loop i in function)")
        if i > maxx:
            maxx = i 
        if i < minn:
            minn = i
    tuples = (minn,maxx)
    return tuples