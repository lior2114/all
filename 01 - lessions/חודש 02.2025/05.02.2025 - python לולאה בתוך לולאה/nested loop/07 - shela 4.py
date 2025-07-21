
for i in range (4): # כדי להגיד כמה ציונים היו בסך הכל לאותו תלמיד לפני שממשיכים לתלמיד הבא  
    total = 0 
    for j in range (3):
        grade = int (input (f"enter a grade:{j+1} of student {i+1} "))
        total += grade
    avg = total / 3
    print (f"the avg of {i+1} student is: {avg} ")