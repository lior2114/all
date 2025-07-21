def get_avarage(lis):
    if len(lis) == 0:
        raise ZeroDivisionError ("!!!youer list is empty!!!")#ZeroDivisionError פשוט שם של בעית האפס שידעו לא משנה זה או ווליו ארור
    summ = 0
    for i in lis:
        if not isinstance(i, (int)):
            raise ValueError("!!!char value!!!!")
        else:
            summ += i
    avg = int(summ / len(lis))
    return avg
