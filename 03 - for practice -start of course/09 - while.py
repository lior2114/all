#עם אחסון מספר
count = 0
s = 0 
while count <= 5:
    num = int(input(f"enter a number {count}: " )) #מציג איזה מספר בסדר אנחנו מכניסים count
    s += num 
    count +=1
print (f"the total of the numbers is: {s}")
