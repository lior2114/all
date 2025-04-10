print("=======A========")
def down(down):
    for i in range(down):
        print(i+1, end = " ")
    print((i+1)*"*")

print("=======B========")
def number(num):
    for i in range(num,0,-1):
        down(i)

n = int(input("enter number: "))
number(n)