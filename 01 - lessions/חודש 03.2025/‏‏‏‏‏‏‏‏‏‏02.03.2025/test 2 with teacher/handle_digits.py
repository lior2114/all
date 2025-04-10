print("=======B=======")
def exist_digits(n, digit):
    if not isinstance(digit,int) or not isinstance(n,int):
        raise ValueError ("enter only numbers!")
    if digit > 9 or digit < 0:
        raise ValueError ("digit is not between 0-9")
    if n < 0:
        n = -1*n # כי אם הוא קטן מ 0 אז מינוס כפול מינוס זה פלוס 
    counter = 0 
    for i in str(n): #123456 => "123456" הופך למחרוזת
        if str(digit) == i:#2 => "2" #הופך למחרוזת
            counter += 1 
        if counter > 2:
            return True
    return False
'''
מכיוון שההשוואה מתבצעת בין מחרוזות ולא בין מספרים
אז בגלל זה עושים את שניהם כ str כדי להפוך אותם למחרוזת של מספרים כדי שנוכל לעבור אחד אחד 
'''

# print("=======B2=======")
# def exist_digitsv2(n2, digit2):
#     if n < 0:
#         n = -1*n # כי אם הוא קטן מ 0 אז מינוס מינוס זה פלוס 
#     if digit2 > 9 or digit2 < 0:
#         raise ValueError ("digit is not between 0-9")
#     if not isinstance(digit2,int) or not isinstance(n2,int):
#         raise ValueError ("enter only numbers!")
#     counter = 0 
#     while n2 > 0:
#         if n2%10 == digit2:
#             counter +=1
#         n2 = n2//10
#     return counter > 2

# # print("=======B3=======")
# def exist_digitsv3(n3, digit3):
#     n3 = abs(n3)# ערך מוחלט הוא הופך אותו לחיובי
#     if digit3 > 9 or digit3 < 0:
#         raise ValueError ("digit is not between 0-9")
#     if not isinstance(digit3,int) or not isinstance(n3,int):
#         raise ValueError ("enter only numbers!")
#     return str(n3).count(str(digit3))>2 # הפכנו למחרוזת וקאונט סופר כמה פעמים הוא בתוכה ואם יותר משתים מחזיר נכון 

