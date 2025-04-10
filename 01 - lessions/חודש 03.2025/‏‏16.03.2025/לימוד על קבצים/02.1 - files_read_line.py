try:
    with open(r"E:\python\works\01 - lessions\חודש 03.2025\‏‏16.03.2025\לימוד על קבצים\lior.txt", 'r') as file:
        currentline = file.readline()
        currentline = currentline.strip()  # מנקה שורות \ רווחים
        print(currentline)
        currentline = file.readline()
        currentline = currentline.strip()  # מנקה שורות \ רווחים
        print(currentline)

except Exception as err:
    print(err)

