import random 
arr = []
for i in range (1,11):
    num = random.randint (10,20) # מספרים רנדומלים מ 10 עד 20
    print (f"the random number: {i} is {num}")
    arr.append(num)
print(arr)


#סורק ערכים של המספר
for num in arr:
    if num > 15:
        print (num, end ="|")

#סורק את המיקומים שלהם ברשימה (אינדקסים)
for i in range (len(arr)):
    # אם המספר שבמיקום שהאיי מסמל אותו גדול מ 15 אז הוא מדפיס אותו 
    if arr[i] > 15:
        print (arr[i], end = "|")
    