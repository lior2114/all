# מדפיס את הסריה ..... 12345 כמה פעמים שמקלידים
n = int (input ("enter a number "))

for i in range (n):
    for j in range (1 , n +1):
        print (j, end = "")
    print ()