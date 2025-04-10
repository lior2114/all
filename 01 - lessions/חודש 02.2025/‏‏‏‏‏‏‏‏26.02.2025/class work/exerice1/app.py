import list_cals

try:
    size = int(input("enter list size: "))
    lis = []
    for i in range(size):
        n = int(input(f"enter number {i+1} for the list: "))
        lis.append(n)    
    av = list_cals.get_avarage(lis)
    print(av)
except ZeroDivisionError as err: #ZeroDivisionError פשוט שם של בעית האפס שידעו לא משנה זה או ווליו ארור
    print(f"value zero: {err}")
except ValueError as err:
    print(f"char error: {err}")