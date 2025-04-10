def perfect_num (n):
    summ = 0 
    for i in range(1,n):
        if n %i == 0:
            summ += i
#  return summ == n: יותר קצר
    if summ == n:
        return True
    return False

def perfect_num_1_10000(n2):
    lis = []
    for i in range(1,n2):
        if perfect_num(i):
            lis.append(i)
    return lis

x = perfect_num_1_10000(10000)
print(x)

# x = perfect_num(7)
# print(x)