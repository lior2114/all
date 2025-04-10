
sum=0 

for i in range (1 , 11):
    numa = int(input(f"enter number {i}: "))
    sum += numa
    i +=1

print(f"the sum is: {sum}")
print(f"the average is: {sum/10}")