# קלט מהמשתמש מספר n
n = int(input("enter a number: "))

# לולאה להצגת משולש מספרים עולים
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()