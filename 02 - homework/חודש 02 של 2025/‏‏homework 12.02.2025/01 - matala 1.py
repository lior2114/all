#א
import random
numrand = []
for i in range (100):
    n = random.randint(1,10)
    numrand.append(n)
print (numrand)
print (f"the length of the list is: {len(numrand)}")
 
 #ב
n2 = int(input ("enter a number if its on te list it will print yes if no then no: "))
if n2 in numrand:
    print(f"yes the number {n2} is on the list") 
else:
    print(f"the number {n2} is not on the list")

#ג
n3 = int(input ("enter a number on the list to know how many time its showing on the list:"))
counter = 0
for i in numrand:
    if i == n3:
        counter += 1
    elif n3 not in numrand:
        print("the number is not on the list") 
        counter = 0   
        break
print(f"the number was on the list {counter} times")

#ד
n4 = int(input ("enter a number to delete from the list: "))
for i in numrand:
    if i == n4:
        numrand.remove(n4)       
else:
    i+=1
print (numrand)
print (f"the length of the list is: {len(numrand)}")

#ה
n5 = int(input ("enter a number to add to the list: "))
list2 = []
list2.append(n5)
for i in numrand:
    if i > n5:
        list2.append(i)
    else:
        i+=1
print(list2)

