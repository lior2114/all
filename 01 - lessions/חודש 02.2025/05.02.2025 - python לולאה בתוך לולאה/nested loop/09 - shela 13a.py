
count = 0 
n = int (input ("enter a number "))
if n == 0:
    count = 1
while n != 0:
    count += 1
    n =  int (n / 10)     # כי אם יש שגיאה שזה פתאום מתחיל לרדת גם למינוס אז זה עוצר אותו כי זה לוקח רק את המספרים החיוביים 
print (f"the {count}")