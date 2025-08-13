import os
from PIL import Image
from tkinter import Tk, filedialog, Toplevel, Label, Entry, Button, StringVar, END

def rename_images(source_files, destination_directory, base_name, custom_name, date, overlay_image_path):
    try:
        # Load the overlay image once
        overlay_image = Image.open(overlay_image_path).convert("RGBA") # Ensure overlay has alpha channel
        # Resize the overlay image to the desired size
        overlay_width = 100  # Set your desired width
        overlay_height = 100  # Set your desired height
        overlay_image = overlay_image.resize((overlay_width, overlay_height))

        # Process each selected file
        for index, source_file in enumerate(source_files):
            # Check if source file exists
            if not os.path.exists(source_file):
                print(f"Error: Source file {source_file} not found.")
                continue

            # Get file extension
            file_extension = os.path.splitext(source_file)[1]
            
            # Construct new file name
            new_name = f"{base_name}{index + 1} - {custom_name} - {date}{file_extension}"
            new_file = os.path.join(destination_directory, new_name)

            # Check if new file name already exists
            if os.path.exists(new_file):
                print(f"Warning: {new_file} already exists. Skipping.")
                continue

            try:
                # Open the original image
                original_image = Image.open(source_file).convert("RGBA") # Ensure base image has alpha channel

                # Calculate the position to paste the overlay image (top-right corner)
                position = (original_image.width - overlay_image.width, 0)

                # Create a transparent layer of the same size as the original image
                transparent_layer = Image.new('RGBA', original_image.size, (0,0,0,0))
                # Paste the overlay onto the transparent layer at the calculated position
                transparent_layer.paste(overlay_image, position)

                # Alpha composite the transparent layer (with the overlay) onto the original image
                combined_image = Image.alpha_composite(original_image, transparent_layer)

                # Save the modified image with the new name
                combined_image.save(new_file)
                print(f"Processed and saved: {new_file}")
            except Exception as img_e:
                 print(f"Error processing file {source_file}: {img_e}")

    except Exception as e:
        print(f"An error occurred: {e}")

def get_all_inputs():
    def browse_source():
        # בחירת מספר קבצי תמונה בבת אחת
        paths = filedialog.askopenfilenames(
            title="בחר תמונות (Ctrl+Click לבחירה מרובה)",
            filetypes=[
                ("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.PNG;*.JPG;*.JPEG;*.GIF;*.BMP"),
                ("All files", "*.*")
            ]
        )
        if paths:
            # שמירת הנתיבים כטקסט מופרד בפסיקים
            source_var.set(";".join(paths))
    def browse_dest():
        path = filedialog.askdirectory(title="בחר תיקיית יעד")
        if path:
            dest_var.set(path)
    def browse_overlay():
        path = filedialog.askopenfilename(
            title="בחר קובץ שכבת-על",
            filetypes=[
                ("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.PNG;*.JPG;*.JPEG;*.GIF;*.BMP"),
                ("All files", "*.*")
            ]
        )
        if path:
            overlay_var.set(path)
    def submit():
        if not all([source_var.get(), dest_var.get(), custom_var.get(), date_var.get(), overlay_var.get()]):
            result_label.config(text="יש למלא את כל השדות", fg="red")
            return
        root.quit()
        root.destroy()
    root = Tk()
    root.title("הגדר נתונים")
    # משתנים
    source_var = StringVar()
    dest_var = StringVar()
    custom_var = StringVar()
    date_var = StringVar()
    overlay_var = StringVar()
    # שורות
    Label(root, text="קבצי מקור:").grid(row=0, column=0, sticky='e')
    Entry(root, textvariable=source_var, width=40).grid(row=0, column=1)
    Button(root, text="בחר", command=browse_source).grid(row=0, column=2)
    Label(root, text="תיקיית יעד:").grid(row=1, column=0, sticky='e')
    Entry(root, textvariable=dest_var, width=40).grid(row=1, column=1)
    Button(root, text="בחר", command=browse_dest).grid(row=1, column=2)
    Label(root, text="שם בסיס:").grid(row=2, column=0, sticky='e')
    Entry(root, textvariable=custom_var, width=40).grid(row=2, column=1, columnspan=2)
    Label(root, text="תאריך:").grid(row=3, column=0, sticky='e')
    Entry(root, textvariable=date_var, width=40).grid(row=3, column=1, columnspan=2)
    Label(root, text="קובץ שכבת-על:").grid(row=4, column=0, sticky='e')
    Entry(root, textvariable=overlay_var, width=40).grid(row=4, column=1)
    Button(root, text="בחר", command=browse_overlay).grid(row=4, column=2)
    result_label = Label(root, text="", fg="red")
    result_label.grid(row=5, column=0, columnspan=3)
    Button(root, text="אישור", command=submit).grid(row=6, column=0, columnspan=3)
    root.mainloop()
    return source_var.get(), dest_var.get(), custom_var.get(), date_var.get(), overlay_var.get()

# --- Main Execution ---
if __name__ == "__main__":
    source_files_str, destination_directory, custom_name, date, overlay_image_path = get_all_inputs()
    # המרת המחרוזת חזרה לרשימת קבצים
    source_files = source_files_str.split(";") if source_files_str else []
    base_name = "ארכיון - תמונה מס' "
    print("\nStarting image processing...")
    rename_images(source_files, destination_directory, base_name, custom_name, date, overlay_image_path)
    print("\nProcessing complete.")