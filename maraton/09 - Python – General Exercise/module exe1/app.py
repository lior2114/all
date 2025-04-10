import limodule as li 
import random

print("========A========")
min = int(input("enter min number: "))
max = int(input("enter max number: "))
my_list = li.minmax_lis(min,max)
print(my_list)

print("========B========")
the_sum = li.sum_lis(my_list)
print(the_sum)

print("========C========")
the_avg = li.avarage_list(my_list)
print(the_avg)

print("========D========")
the_splited = li.split_numbers(my_list)
print(the_splited)

print("========E========")
prime_numbers = li.prime_number(my_list)
print(prime_numbers)

print("========F========")
perfect_numbers = li.perfect_number(my_list) #כאן עשיתי הצגה של המספרים מתוך הרשימה אם הם מספרים מושלמים פשוט היה לי יותר נוח להבין 
print(perfect_numbers)

print("========F========")
number = int(input("Enter a number: "))
perfect = li.next_perfect_number(number)
print(perfect)

print("========H========")
print(li.perfect_10000())

print("========I========")
listed1 = [1, 8, 1] 
listed2 =  [100,200,1,2,400, 8] 
truefalse = li.two_list(listed1,listed2)
print(truefalse)

print("========J======")
num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
reverse = li.reverse_numbers(num1,num2)
print(reverse)

print("========K======")
sen1 = input("enter sentence1: ")
sen2 = input("enter sentence2: ")
equal_sen = li.some_sentences(sen1,sen2)
print(equal_sen)


print("========L12======")
matriz = []
for i in range(3):
    for rows in range(3):
        num = random.randint(1,2)
        matriz.append(num)
print(matriz)
avgminmax = li.some_matriza(matriz)
print(avgminmax)

print("========M======")
listed = [110,-203]
somelist = li.somelisted(listed)
print(somelist)

print("========N======")
n = int(input("enter serials numbers: "))
not_in_numbers = li.down_number_not_exist(n)
print(not_in_numbers)