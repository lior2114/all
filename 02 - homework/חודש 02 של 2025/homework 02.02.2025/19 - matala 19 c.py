#מספר ראשוני - מספר שמתחלק בעצמו וב -1 בלבד. 2 ו 1 נחשבים ראשוניים.
 # מספר יכול להתחלק רק במספר הקטן ממנו 
 # מספר יכול להתחלק רק במספר קטן ממחצית המספר 
 # מספר מתחלק במספר הקטן מהשורש הריבועי שלו 
import math 
n = int(input("enter a number: "))
its_prime =True
for i in range(2, int (math.sqrt (n))):
    if n % i == 0:
        #print (i , end = "|")
        its_prime = False
        break 
if its_prime:
    print(f"{n} its a prime number")
else: 
    print(f"{n} its not a prime number")