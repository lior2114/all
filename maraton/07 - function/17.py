print("=======A========")
def down (number):
    for i in range(number):
        print("*",end = " ")
    print()
    
print("=======B========")
def run_on_number(ran):
    for i in range(ran,0,-1):
        down(i)

num = int(input("enter number: "))
run_on_number(num)