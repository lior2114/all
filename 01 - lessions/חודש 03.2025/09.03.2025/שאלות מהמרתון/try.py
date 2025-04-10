rohav = int(input("enter rohav: "))
high = int(input("enter high: "))
print('*' * rohav)
for i in range(high - 2):
    print('*'+' '*(rohav -2) + '*')
print('*' * rohav)