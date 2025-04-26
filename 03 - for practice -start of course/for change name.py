import os

def rename_images(directory, base_name, custom_name, date):
    try:
        # Get list of files in the directory
        files = os.listdir(directory)
        # Filter out only image files (assuming jpg and png for this example)
        image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
        
        # Sort files to ensure consistent numbering
        image_files.sort()
        
        # Rename each image file
        for index, filename in enumerate(image_files):
            # Construct new file name
            new_name = f"{base_name}{index + 1} - {custom_name} - {date}{os.path.splitext(filename)[1]}"
            # Get full file paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)
            
            # Check if new file name already exists
            if os.path.exists(new_file):
                print(f"Error: {new_file} already exists.")
                continue
            
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {old_file} to {new_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory = r'C:\Users\Lior\Desktop\תמונות' #המיקום של הקובץ
base_name = 'ארכיון - תמונה מס\' '
custom_name = 'בסיס צאלים'
date = '02.11.2023'  # Set the date manually

rename_images(directory, base_name, custom_name, date)
