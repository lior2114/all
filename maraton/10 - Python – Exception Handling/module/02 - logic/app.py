import range_operations as ra
try:
    '''
    כי אם נכניס על אינט או פלואט אות זה ישר יקרוס מבלי להגיע לבעיה 
    כי אי אפשר להכניס לאינט אות לכן נתחיל ממחזרוזת שיוכל כן לקבל את אותה האות 
    ואז זה עובר דרך הבעיה ובודק אם יש אות או מספר 
    זה גם פוטר מינוסים 
    ומספרים עם נקודות
    '''
    size = input("enter the size of the list: ") # מתחילים ממחרוזת כדי לבדוק אם יש אותיות 
    if not size.isdigit():
        raise TypeError ("enter only numbers! (size)")
    new_size = int(size)

    minn = input("enter min number to start: ")
    if not minn.isdigit():
        raise TypeError ("enter only numbers! (minn)")
    new_minn = int(minn)

    maxx = input("enter max number to stop: ")
    if not maxx.isdigit():
        raise TypeError ("enter only numbers! (max)")
    new_maxx = int(maxx)
    random_list = ra.generate_list(new_size,new_minn,new_maxx)
    print(random_list)


except ValueError as err:
    print(err)
except TypeError as err:
    print(err)
except Exception as err:
    print(err)