fruit =  []
for i in range (3):
    f = input(f"enter name of fruit {i}:  ")
    fruit.append(f) #מוסיף את השם לליסט של הפירות בסוגרים הריקים למעלה 
print ("the fruits is: " , fruit)

#א
#כל פעם מציג לי פרי שונה f
for f in fruit:
    #  מציג את האורך של המילה     מציג את המילה
    print(f, "lengh is: ", {len(f)})

#ב
for i in range (len(fruit)):
    #     האורך של המילה הראשונה            המילה הראשונה
    print(fruit[i] ,"length is: ", {len(fruit[i])})

counter = 0 
for f in fruit:
    counter+=len(f)
print("the sum of all the letters in the fruits is: ", counter)
