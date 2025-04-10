#פונקציה שמחזירה את סכום הספרות במספר
def sum_digits (number):
    if not isinstance(number,int):
        raise ValueError ("please enter integer! ")
    number = abs (number) # שאם יכנס מספר שלילי אז הוא יהפוך אותו לחיובי ולא יקרוס 
    number = str(number)
    sum = 0 
    for digit in number:
        sum +=int(digit)
    return sum
# אופציה 2
    while number!= 0: 
        print(number)
        sum =sum + number%10
        number=number//10
