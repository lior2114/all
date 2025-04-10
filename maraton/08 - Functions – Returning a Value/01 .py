print("========A========")
def lis(li):
    summ = 0
    counter = 0 
    for i in li:
        summ += i 
        counter += 1
    avg = (summ / counter)
    return avg 

print("========B========")
for i in range(3):
    lsitt = []
    for j in range(3):
        n = int(input(f"Enter number {j + 1} for list {i + 1}: "))
        lsitt.append(n)
    x = lis(lsitt)
    print(f"Average of list {i + 1}: {x}")
