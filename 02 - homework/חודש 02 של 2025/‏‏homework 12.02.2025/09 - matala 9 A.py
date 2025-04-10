import random

#שיטה א bucket
lis = [1,2,3,2,5,9,2,1,1,3]
# buckets = [0,0,0,0,0,0,0,0,0,0,0,0]
#              1,2,3,4,5,6,7,8,9,10               
# buckets = [0,3,3,2,0,1,0,0,0,1,0]
bucket = []
for num in range(11):
    bucket.append(0) # יוצר רשימה של 11 איברים כולם 0
for num in lis:
    bucket[num] += 1 # מוסיף 1 למספר המופיע ברשימה של האפסים
print(bucket)

max = bucket[0]
for num in bucket:
    if num > max:
        max = num

arrmax = []
for i in range(len(bucket)):
    if bucket[i] == max:
        arrmax.append(i)
print(arrmax)