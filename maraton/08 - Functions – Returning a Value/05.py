print("==========A=========")
def some_numbers(lis):
    avg = sum(lis) / len(lis)
    counter = 0
    for i in lis:
        if i >= avg:
            counter += 1
    return counter 

print("==========B=========")
for i in range(3):
    number_list = []
    for j in range(3):
        n = int(input(f"enter number {j+1} for list {i+1}: "))
        number_list.append(n)
    x = some_numbers(number_list)
    print(f"there are {x} numbers that are greater than or equal to the average of the list")
