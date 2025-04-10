sentence = "i love list"
chars = {}
print(sentence)
for ch in sentence:
    print(ch , end = " ")
    if ch == " ":
        continue
    #בודק אם ch נמצא בדיקשינרי
    if ch in chars:
        chars[ch] +=1 #מעלה את הוליו של האות ב1
    else:
        chars[ch] = 1
print(chars)

max_key = ""
max_value = 0
for key , value in chars.items():#items זה פונקציה שמחזירה רשימה של כל האיברים במילון
    if value > max_value:
        max_value = value
        max_key = key
print(f"the most common char is {max_key} and it appears {max_value} times")