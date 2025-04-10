sum =0  
for i in range(10): 
    number = int(input("enter a number: "))
    sum += number # = sum =sum +number מאחסן אותו בתוך sum
    exit = input("enter exit or any key to stop")
    if exit == "exit": 
        break
print(f"sum of the numbers is {sum}") 
avg = sum / (i+1) #כי i מתחיל מ 0 
print (f"avg is {avg}")