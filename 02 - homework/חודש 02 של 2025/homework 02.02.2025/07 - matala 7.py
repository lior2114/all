numa = int(input("enter number A: "))
numb = int(input("enter number B: "))

for i in range (numa , numb+1):
    if i % 2:
     continue
    print (i)