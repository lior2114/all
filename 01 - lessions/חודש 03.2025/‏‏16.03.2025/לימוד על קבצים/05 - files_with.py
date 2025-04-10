with open(r"E:\python\works\01 - lessions\חודש 03.2025\‏‏16.03.2025\לימוד על קבצים\lior.txt", 'a') as file:
    file.write("i love israel\n")

'''
with סוגר אוטומטית את הקובץ

נשתמש בו בגלל המצב הנ"ל:
'''
try:
    file = open(r"E:\python\works\01 - lessions\חודש 03.2025\‏‏16.03.2025\לימוד על קבצים\lior.txt", 'a')
    file.write("i love israel\n")
    x = int(input("enter number: ")) # אם נכנס האות b יהיה שגיאה 
    file.close() # בגלל ששורה קודמת היה שגיאה אז הוא לא הגיע לשורה לסגירה של הקובץ אז לשם כך נועד ה with
except Exception as err:
    print(err)
