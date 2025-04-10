print("========A========")
def lis(li):
    min = float("inf")
    for i in li:
        if i <= min:
            min = i 
    return min
        
for i in range(3):
    listt = []
    for j in range(3):
        n = int(input(f"enter number {j+1} for list number {i+1}: "))
        listt.append(n)
    x = lis(listt)
    print(f"the min number of list {i+1} is {x}")