numbers = [-1,-20,-30,-2,-4]
#               מתחיל מהמקום ה 0 ברשימה כדי שלא יתחיל ממספר 0 ואז במינוסים זה יגיד שהכי גבוה זה 0 כי 0 יותר גדול ממינוס  
#אופציה א
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print("the max number is: ", max_num)

#אופציה ב
print ("the max number is: ", max(numbers))