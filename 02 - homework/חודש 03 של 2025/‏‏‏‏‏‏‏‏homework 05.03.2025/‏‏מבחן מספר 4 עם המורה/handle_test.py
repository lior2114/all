def is_prime(n):
    if n <= 1:
        return False
    if n == 2: 
        return True
    for i in range(2,n):
        if n % i == 0: 
            return False
    return True
    
def for_list(lis):
    if len(lis) == 0:
        raise ValueError ("list is empty! (in for_list function)")
    new_lis= []
    for index, value in enumerate(lis):
        if is_prime(value):
            new_lis.append((value, index))
        else:
            continue
    print(len(new_lis))
    return new_lis


