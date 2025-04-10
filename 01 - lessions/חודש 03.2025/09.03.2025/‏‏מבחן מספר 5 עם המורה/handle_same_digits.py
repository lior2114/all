def not_same_digits(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    number = abs(number)
    number_str = str(number)

    if len(number_str) == 1:
        return True
    
    some_list = []
    for digit in number_str:
        if digit in some_list:
            return False
        some_list.append(digit)
    return True

    #אופציה 2 
    def not_same_digits(n):
        number = []
        n = abs(n)
        n = str(n)
        for digit in n:
            if digit not in number:#334
                number.append(digit)
    return len(number) == len(n)
 #          [3,4]       [3,3,4]   =  false

    #אופציה 3 
    def not_same_digits(n):
        n =abs(n)
        n =str(n)
    return (len(set(n))) == len(n)
