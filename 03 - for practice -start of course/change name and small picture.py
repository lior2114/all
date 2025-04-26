import os
from PIL import Image

def rename_images(directory, base_name, custom_name, date, overlay_image_path):
    try:
        # Get list of files in the directory
        files = os.listdir(directory)
        # Filter out only image files (assuming jpg and png for this example)
        image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
        
        # Sort files to ensure consistent numbering
        image_files.sort()
        
        # Load the overlay image
        overlay_image = Image.open(overlay_image_path)
        overlay_image = overlay_image.resize((285, 285))
        
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
            
            # Open the original image
            original_image = Image.open(old_file)
            
            # Paste the overlay image onto the original image
            original_image.paste(overlay_image, (original_image.width - 285, 0), overlay_image)
            
            # Save the modified image with the new name
            original_image.save(new_file)
            print(f"Renamed and modified: {old_file} to {new_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory = r'C:\Users\Lior\Desktop\תמונות' #המיקום של הקובץ
base_name = 'ארכיון - תמונה מס\' '
custom_name = 'בסיס צאלים'
date = '02.11.2023'  # Set the date manually
overlay_image_path = r'C:\overlay\sc.png'  # Path to the overlay image

rename_images(directory, base_name, custom_name, date, overlay_image_path)