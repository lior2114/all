import os
from tkinter import Tk, filedialog, Label, Entry, Button, StringVar

def rename_files_in_directory(directory_path, base_name, custom_name, date):
    try:
        # Get all files in the directory
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        
        # Filter for image files
        image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.PNG', '.JPG', '.JPEG', '.GIF', '.BMP']
        image_files = [f for f in files if any(f.lower().endswith(ext.lower()) for ext in image_extensions)]
        
        if not image_files:
            print("לא נמצאו קבצי תמונה בתיקייה הנבחרת.")
            return
        
        print(f"נמצאו {len(image_files)} קבצי תמונה לעיבוד...")
        
        # Process each image file
        for index, filename in enumerate(image_files):
            # Get file extension
            file_extension = os.path.splitext(filename)[1]
            
            # Construct new file name
            new_name = f"{base_name}{index + 1} - {custom_name} - {date}{file_extension}"
            old_file = os.path.join(directory_path, filename)
            new_file = os.path.join(directory_path, new_name)

            # Check if new file name already exists
            if os.path.exists(new_file):
                print(f"אזהרה: {new_name} כבר קיים. דילוג.")
                continue

            try:
                # Rename the file
                os.rename(old_file, new_file)
                print(f"שונה שם: {filename} -> {new_name}")
            except Exception as e:
                print(f"שגיאה בעת שינוי שם הקובץ {filename}: {e}")

    except Exception as e:
        print(f"אירעה שגיאה: {e}")

def get_inputs():
    def browse_directory():
        path = filedialog.askdirectory(title="בחר תיקייה עם קבצי תמונה")
        if path:
            directory_var.set(path)
    
    def submit():
        if not all([directory_var.get(), custom_var.get(), date_var.get()]):
            result_label.config(text="יש למלא את כל השדות", fg="red")
            return
        root.quit()
        root.destroy()
    
    root = Tk()
    root.title("שינוי שמות קבצים")
    
    # משתנים
    directory_var = StringVar()
    custom_var = StringVar()
    date_var = StringVar()
    
    # שורות
    Label(root, text="תיקייה:").grid(row=0, column=0, sticky='e')
    Entry(root, textvariable=directory_var, width=40).grid(row=0, column=1)
    Button(root, text="בחר", command=browse_directory).grid(row=0, column=2)
    
    Label(root, text="שם בסיס:").grid(row=1, column=0, sticky='e')
    Entry(root, textvariable=custom_var, width=40).grid(row=1, column=1, columnspan=2)
    
    Label(root, text="תאריך:").grid(row=2, column=0, sticky='e')
    Entry(root, textvariable=date_var, width=40).grid(row=2, column=1, columnspan=2)
    
    result_label = Label(root, text="", fg="red")
    result_label.grid(row=3, column=0, columnspan=3)
    
    Button(root, text="אישור", command=submit).grid(row=4, column=0, columnspan=3)
    
    root.mainloop()
    return directory_var.get(), custom_var.get(), date_var.get()

# --- Main Execution ---
if __name__ == "__main__":
    directory_path, custom_name, date = get_inputs()
    
    if directory_path and custom_name and date:
        base_name = "ארכיון - תמונה מס' "
        print("\nמתחיל עיבוד קבצים...")
        rename_files_in_directory(directory_path, base_name, custom_name, date)
        print("\nהעיבוד הושלם.")
    else:
        print("הפעולה בוטלה.")