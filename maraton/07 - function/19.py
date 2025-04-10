print("=======A========")
def down(down):
    for i in range(down):
        print('*',end = "")
    print()

def ups(up):
    for i in range(1,up+1):
        print('*',end = "")
    print()

def number(num):
    for i in range(num,0,-1):
        down(i)
    for i in range(1,num+1):
        ups(i)
    
n = int(input("enter number: "))
number(n)