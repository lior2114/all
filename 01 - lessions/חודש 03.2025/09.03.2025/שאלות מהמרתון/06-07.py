def perfect_num (n):
    summ = 0 
    for i in range(1,n):
        if n %i == 0:
            summ += i
#  return summ == n: יותר קצר
    if summ == n:
        return True
    return False

def next_perfect_num (n2):
    new = n2+1
    while not perfect_num(new):
        new=new+1
    return new

print(next_perfect_num(6))

# x = perfect_num(7)
# print(x)