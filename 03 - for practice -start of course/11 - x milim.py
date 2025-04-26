# Get width and height from the user
width = int(input("Enter the width of the rectangle: "))
height = int(input("Enter the height of the rectangle: "))

# Print the rectangle
for i in range(height):
    print('*' * width)