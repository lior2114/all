while True: #לא חובה רק שם בתוך לולאה
    try:
        grades = [100,90,80,60,40,100]
        index = int(input("enter number of your student search for grade: "))
        print(f"Grade of your student is: {grades[index]}")
    except:
        print("please enter right value")