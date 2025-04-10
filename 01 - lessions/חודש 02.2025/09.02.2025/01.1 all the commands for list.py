# Creating a sorted list of 5 numbers
sorted_list = [1, 2, 3, 4, 5]  # יצירת רשימה מסודרת של 5 מספרים

# Adding an element to the end of the list
sorted_list.append(6)  # הוספת איבר לסוף הרשימה
# Example: sorted_list = [1, 2, 3, 4, 5, 6]

# Extending the list by appending elements from another list
sorted_list.extend([7, 8, 9])  # הרחבת הרשימה על ידי הוספת איברים מרשימה אחרת
# Example: sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Inserting an element at a specific position
sorted_list.insert(0, 0)  # הוספת איבר במיקום מסוים
# Example: sorted_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Removing the first occurrence of an element
sorted_list.remove(3)  # הסרת ההופעה הראשונה של איבר
# Example: sorted_list = [0, 1, 2, 4, 5, 6, 7, 8, 9]

# Removing an element at a specific position
sorted_list.pop(2)  # הסרת איבר במיקום מסוים
# Example: sorted_list = [0, 1, 4, 5, 6, 7, 8, 9]

# Removing the last element
sorted_list.pop()  # הסרת האיבר האחרון
# Example: sorted_list = [0, 1, 4, 5, 6, 7, 8]

# Finding the index of the first occurrence of an element
index = sorted_list.index(4)  # מציאת האינדקס של ההופעה הראשונה של איבר
# Example: index = 2

# Counting the occurrences of an element
count = sorted_list.count(2)  # ספירת ההופעות של איבר
# Example: count = 1

# Sorting the list
sorted_list.sort()  # מיון הרשימה
# Example: sorted_list = [0, 1, 4, 5, 6, 7, 8]

# Reversing the list
sorted_list.reverse()  # היפוך הרשימה
# Example: sorted_list = [8, 7, 6, 5, 4, 1, 0]

# Copying the list
new_sorted_list = sorted_list.copy()  # העתקת הרשימה
# Example: new_sorted_list = [8, 7, 6, 5, 4, 1, 0]

# Clearing all elements from the list
sorted_list.clear()  # ניקוי כל האיברים מהרשימה
# Example: sorted_list = []