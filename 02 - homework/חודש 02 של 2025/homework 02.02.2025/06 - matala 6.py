num = int(input("enter a number: "))
  
for i in range(0, num+1):
    if i % 10 == 5:
     continue
    print(i)
