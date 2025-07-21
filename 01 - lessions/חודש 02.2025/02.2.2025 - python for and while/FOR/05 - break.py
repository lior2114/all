sum =0  
for i in range (10): 
    number = int (input ("enter a number or 0 to break "))
    sum += number # = sum =sum +number מאחסן אותו בתוך sum 
    if number == 0: 
        break
print (f"sum of the numbers is {sum}")
avg = sum / 10  
print (f"avg is {avg}")    