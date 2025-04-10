def get_average(lis):
    if len(lis) == 0:
        raise ValueError ("list empty")
    summ = sum(lis)
    counter = 0
    for i in lis:
        if not isinstance(i,int):
            raise TypeError ("enter only numbers")
        counter +=1
    return(summ/counter)

