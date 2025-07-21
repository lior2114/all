for i in range(1,11):
    number = int(input("enter a number: "))
    if number %2 == 0: #אם המספר שהוכנס זוגי ממשיכים כי אם הוא מתחלק בשתים ואין לו שארית אז ממשיך 
        continue 
    print (f"i love {number}")
