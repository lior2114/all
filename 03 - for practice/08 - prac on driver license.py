age = float(input("enter your age: "))
exp = float(input("enter your exprience: "))

if age < 18:
    print ("you are too old to get driver license")
elif age >=18 and age <=21:
    if exp >=1:
        print ("you can get driver license")
    else:
        exp-=1
        print ("you will have to wait another", exp , "years")
        if age > 21:
            print ("you can get driver license no limits")