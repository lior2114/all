counter = 0 
n = int (input ("enter a number: "))
while n != 0: 
    counter += 1
    n =n // 10 #  אם יש שגיאה שזה פתאום מתחיל לרדת גם למינוס אז זה עוצר אותו כי זה לוקח רק את המספרים אם השארית 0 
print (f"the {counter}")