def sriria(n):
    for i in range(1, n + 1):
        # הדפסת הרווחים בתחילת השורה
        print(" " * (n - i) * 2, end="")
        
        # הדפסת המספרים העולים
        for j in range(1, i + 1):
            print(j, end=" ")
        
        # הדפסת המספרים היורדים
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        
        # מעבר לשורה הבאה
        print()

n = int(input("enter number: "))
sriria(n)