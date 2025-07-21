import random
numbers = []
for i in range (1,11):
    num = random.randint (-50,50)
    numbers.append(num)
print(numbers)

# אופצית סכום א
s= sum(numbers)
print("the sum of all numbers opzia A is: ", s)

# אופציה ממוצע א 
avg = s/len(numbers)
print("the avg of all numbers opzia A is: ", s)




# אופצית סכום ב
sum =0 
#  מייצג כל פעם כל מספר שברשימה
for num in numbers:
    sum+=num
print("the sum of all numbers opzia B is: ", sum )

#אופצית ממוצע ב 
#                           הלין זה כמה סך הכל מספרים יש לנו ברשימה 
print ("the avg of all numbers opzia B  is: ", sum/len(numbers))