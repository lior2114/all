def is_prime(n):
    n = abs(n)
    if n == 2:
        return True
    for i in range(2,n): # (2,int(n/2)-1) מחלקים בחצי כי מספר לא יכול להתחלק יותר מהחצי שלו אז זה חוסך 
        if n%i == 0:
            return False
    return True

def from_list(min,max):
    if min > max:
        min,max = max,min
    lis = []
    for i in range(min,max,1):
        if is_prime(i):
            lis.append(i)
    return lis

x = from_list(10,100)
print(x)
print(len(x))
