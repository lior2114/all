def avarage_and_sum(li):
    if len(li) == 0:
        raise ValueError ("list empty! (in handle_list)")
    for i in li:
        if not isinstance (i,int):
            raise ValueError ("enter only numbers!(in handle_list) ")
    s = sum(li)
    av = s / len(li)
    dic = {"avg":int(av), "sum":s}
    return dic
