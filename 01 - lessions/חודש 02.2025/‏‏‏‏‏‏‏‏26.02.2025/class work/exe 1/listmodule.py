def do_list(n1,n2):
    if n1 > n2:
        n1,n2 = n2,n1 #switch
    liss = []
    for i in range(n1,n2):
        liss.append(i)
    return liss

def sum_list(listt):
    return sum(listt)

def avg(listt):
    if len(listt) == 0:
        return 0
    summ = 0
    counter = 0
    for i in listt:
        summ += i
        counter += 1
    avarage = summ / counter
    return avarage

def split(listt):
    l = []
    counter = 0
    for i in listt:
        if i %2 ==  0:
            l.append(i)
            counter += 1
        else:
            i +=1
    return l,counter

