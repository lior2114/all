print("==========A=========")
def some_numbers(lis):
    min_number = float("inf")
    min_index = -1 #אתחול האינדקס למינוס אחד כי אם נשווה ל 0 יחשבו שהאינקס המינימלי נמצא במקום - כי הרשימה מתחילה מ 0 
    for i in range(len(lis)):
        if lis[i] < min_number:
            min_number = lis[i]
            min_index = i
    return min_index

print("==========B=========")
for minimun in range(3):
    listed = []
    for j in range(3):
        n = int(input(f"enter number {j+1} for list {minimun+1}: "))
        listed.append(n)
    x = some_numbers(listed)
    print(f"The index of the minimum number in list {minimun+1} is: {x}")
