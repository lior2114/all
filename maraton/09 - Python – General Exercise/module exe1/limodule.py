print("========A========")
def minmax_lis(min,max):
    listed = []
    if min > max:
        min,max = max,min 
    for i in range(min,max+1):
        listed.append(i)
    return listed

print("========B========")
def sum_lis(s):
    return sum(s)

print("========C========")
def avarage_list(a):
    return (sum(a)/len(a))

print("========D========")
def split_numbers(sp):
    spl = []
    for i in sp:
        if i%2 == 0:
            spl.append(i)
    return spl 

print("========E========")
def prime_number(pr):
    prime_list = []
    for i in pr:
        if i > 1:
            for j in range(2,i):
                if i%j == 0:
                    break 
            else:
                prime_list.append(i)
    return (prime_list)

print("========F========")
def perfect_number(perf):
    perfect_list = []
    for i in perf:
        if i > 0: 
            summ = 0 
            for j in range(1, i): 
                if i % j == 0:
                  summ+=j
            if summ == i:
                perfect_list.append(summ)
    return perfect_list


print("========G========")
def next_perfect_number(n):
    def is_perfect(num):
        list_perfect = []
        summ = 0 #בגלל שאנחנו רצים על מספר אז זה יהיה מחוץ ללולאה כדי שלא כל פעם יתאפס ל 0 שם
        for i in range(1, num): 
            if num % i == 0:
                summ += i
        if summ == num:                
            return summ

    num = n+1
    while True:
        if is_perfect(num):
            return num
        num += 1

print("========H========")
def perfect_10000():
    perfect_10000 = []
    for i in range(1, 10000):
        summ = 0 
        for j in range(1, i):#מתחילים מאחד כדי להימנע מחילוק ב 0 
            if i % j == 0:
                summ += j
        if summ == i: 
            perfect_10000.append(i)
    return perfect_10000

print("========I========")
def two_list(list1, list2):
    for i in list1:
        if i not in list2:
            return False
    return True

print("========J========")
def reverse_numbers(num1, num2):
    reversed_num1 = 0
    while num1 > 0:
        digit = num1%10
        reversed_num1 = reversed_num1 * 10 + digit
        num1 = num1//10 

    return reversed_num1 == num2 # כי אם נכנס 123 ו 321 אז זה הופך את המספר 123 ל 321 כי עשינו פעולת הפיכה אז יוצא שהם שווים
'''
הפיכת מספר לסדר ההפוך שלו 
'''
# def reverse_number(num):
#     reversed_num = 0
#     while num > 0:
#         digit = num % 10
#         reversed_num = reversed_num * 10 + digit #הכפלה ב 10 כדי שנוכל להוסיף את המספר הבא בלי שהוא ישנה את הקודם שכבר התווסף
#         num = num // 10
#     return reversed_num



print("========K========")
def some_sentences(sen1, sen2):
    return sen2 in sen1


print("========L========")
def some_matriza(matriz):
    summ = 0
    counter = 0
    maxx = 0 
    minn = float('inf')
    for i in matriz:
        for j in matriz:
            summ += j
            counter += 1
            if j > maxx:
                maxx = j 
            if j < minn:
                minn = j 
    avarage = summ /counter
    tuples = (avarage,maxx,minn)
    return tuples

print("========M======")
def somelisted (listed):
    counter = 0 
    for i in listed: #     str ממיר את הרשימה למחרוזת ואז אפשר לפצל אותה 
        counter += len(str(abs(i))) #abs מספר אבסולוטי כדי להימנע ממינוסים
    return counter

print("========N======")
def down_number_not_exist(numbers):
    listed = []
    new_list = set(range(1, 10))#יצירת סט מ 1-10 סט כדי שלא יחזרו אותם מספרים פעמיים
    while numbers > 0:
        digit = numbers % 10
        listed.append(digit)
        numbers = numbers // 10
    for i in listed:
        if i in new_list: # אם אותו מספר לא נמצא בסט
            new_list.remove(i)#תמחק אותו מהסט של מ 1-10
    new_list = list(new_list)
    new_list.reverse()
    return(new_list)

