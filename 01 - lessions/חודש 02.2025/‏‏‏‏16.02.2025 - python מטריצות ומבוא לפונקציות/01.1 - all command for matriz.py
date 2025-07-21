import numpy as np

# יצירת מטריצה מאפסים בגודל 3x3
matrix_zeros = np.zeros((3, 3))  # np.zeros יוצרת מטריצה מלאה באפסים בגודל הנתון
print(matrix_zeros)

# יצירת מטריצה מלאה באחדות בגודל 3x3
matrix_ones = np.ones((3, 3))  # np.ones יוצרת מטריצה מלאה באחדות בגודל הנתון
print(matrix_ones)

# יצירת מטריצה ריקה בגודל 3x3 (ערכים אקראיים)
matrix_empty = np.empty((3, 3))  # np.empty יוצרת מטריצה ריקה בגודל הנתון (ערכים אקראיים)
print(matrix_empty)

# יצירת מטריצה עם ערכים רנדומליים בגודל 3x3
matrix_random = np.random.random((3, 3))  # np.random.random יוצרת מטריצה עם ערכים רנדומליים בגודל הנתון
print(matrix_random)

# יצירת מטריצה עם ערכים קבועים בגודל 3x3
matrix_full = np.full((3, 3), 7)  # np.full יוצרת מטריצה עם ערכים קבועים בגודל הנתון
print(matrix_full)

# יצירת מטריצה זהות בגודל 3x3
matrix_identity = np.eye(3)  # np.eye יוצרת מטריצה זהות בגודל הנתון
print(matrix_identity)

# חישוב סכום של מטריצה
matrix_sum = np.sum(matrix_ones)  # np.sum מחשבת את הסכום של כל הערכים במטריצה
print(matrix_sum)

# חישוב ממוצע של מטריצה
matrix_mean = np.mean(matrix_ones)  # np.mean מחשבת את הממוצע של כל הערכים במטריצה
print(matrix_mean)

# חישוב מטריצה טרנספוזית
matrix_transpose = np.transpose(matrix_ones)  # np.transpose מחשבת את הטרנספוז של המטריצה
print(matrix_transpose)

# חישוב דטרמיננטה של מטריצה
matrix_det = np.linalg.det(matrix_identity)  # np.linalg.det מחשבת את הדטרמיננטה של המטריצה
print(matrix_det)

# חישוב אינברס של מטריצה
matrix_inv = np.linalg.inv(matrix_identity)  # np.linalg.inv מחשבת את האינברס של המטריצה
print(matrix_inv)