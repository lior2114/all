import os
import json
import threading
from PIL import Image
from tkinter import Tk, filedialog, Toplevel, Label, Entry, Button, StringVar, END, messagebox, ttk

# קובץ הגדרות
SETTINGS_FILE = "overlay_settings.json"

def save_settings(overlay_path, overlay_width, overlay_height, margin_top, margin_right):
    """שמירת הגדרות לקובץ JSON"""
    settings = {
        "overlay_path": overlay_path,
        "overlay_width": overlay_width,
        "overlay_height": overlay_height,
        "margin_top": margin_top,
        "margin_right": margin_right
    }
    try:
        with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
            json.dump(settings, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"שגיאה בשמירת הגדרות: {e}")

def load_settings():
    """טעינת הגדרות מקובץ JSON"""
    default_settings = {
        "overlay_path": "",
        "overlay_width": 100,
        "overlay_height": 100,
        "margin_top": 10,
        "margin_right": 10
    }
    
    try:
        if os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
                settings = json.load(f)
                # וידוא שכל המפתחות קיימים
                for key in default_settings:
                    if key not in settings:
                        settings[key] = default_settings[key]
                return settings
    except Exception as e:
        print(f"שגיאה בטעינת הגדרות: {e}")
    
    return default_settings

def show_progress_window(total_files, callback):
    """יצירת חלון progress bar"""
    progress_window = Tk()
    progress_window.title("מעבד תמונות...")
    progress_window.geometry("400x150")
    progress_window.resizable(False, False)
    
    # משתנים גלובליים
    is_cancelled = False
    
    # מרכיבי החלון
    Label(progress_window, text="מעבד תמונות...", font=("Arial", 12)).pack(pady=10)
    
    progress_var = StringVar(value="0/0")
    progress_label = Label(progress_window, textvariable=progress_var, font=("Arial", 10))
    progress_label.pack(pady=5)
    
    progress_bar = ttk.Progressbar(progress_window, length=300, mode='determinate')
    progress_bar.pack(pady=10)
    progress_bar['maximum'] = total_files
    
    status_label = Label(progress_window, text="מתחיל עיבוד...", font=("Arial", 9))
    status_label.pack(pady=5)
    
    def cancel_callback():
        nonlocal is_cancelled
        is_cancelled = True
        progress_window.destroy()
    
    # כפתור ביטול
    cancel_button = Button(progress_window, text="ביטול", command=cancel_callback)
    cancel_button.pack(pady=10)
    
    # הפעלת העיבוד ב-thread נפרד
    def run_processing():
        try:
            callback(progress_var, progress_bar, status_label, lambda: is_cancelled)
        except Exception as e:
            print(f"שגיאה בעיבוד: {e}")
        finally:
            # עדכון UI ב-main thread
            progress_window.after(0, lambda: progress_window.destroy())
    
    thread = threading.Thread(target=run_processing, daemon=True)
    thread.start()
    
    # הפעלת החלון
    progress_window.mainloop()
    
    return is_cancelled

def rename_images(source_directory, destination_directory, base_name, custom_name, date, overlay_image_path, overlay_width, overlay_height, margin_top, margin_right, progress_var=None, progress_bar=None, status_label=None, is_cancelled_func=None):
    try:
        # Get list of files in the source directory
        files = os.listdir(source_directory)
        # Filter out only image files (assuming jpg and png for this example)
        image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

        # Sort files to ensure consistent numbering
        image_files.sort()

        # Load the overlay image
        overlay_image = Image.open(overlay_image_path).convert("RGBA") # Ensure overlay has alpha channel
        # Resize the overlay image to the desired size
        overlay_image = overlay_image.resize((overlay_width, overlay_height))

        # Rename each image file
        for index, filename in enumerate(image_files):
            # בדיקת ביטול
            if is_cancelled_func and is_cancelled_func():
                break
                
            # עדכון progress bar
            if progress_var and progress_bar and status_label:
                progress_var.set(f"{index + 1}/{len(image_files)}")
                progress_bar.config(value=index + 1)
                status_label.config(text=f"מעבד: {filename}")
            
            # Construct new file name
            new_name = f"{base_name}{index + 1} - {custom_name} - {date}{os.path.splitext(filename)[1]}"
            # Get full file paths
            old_file = os.path.join(source_directory, filename)
            new_file = os.path.join(destination_directory, new_name)

            # Check if new file name already exists
            if os.path.exists(new_file):
                print(f"Warning: {new_file} already exists. Skipping.")
                continue

            try:
                # Open the original image
                original_image = Image.open(old_file).convert("RGBA") # Ensure base image has alpha channel

                # Calculate the position to paste the overlay image (top-right corner with margins)
                x = original_image.width - overlay_image.width - margin_right
                y = margin_top
                position = (x, y)

                # Create a transparent layer of the same size as the original image
                transparent_layer = Image.new('RGBA', original_image.size, (0,0,0,0))
                # Paste the overlay onto the transparent layer at the calculated position
                transparent_layer.paste(overlay_image, position)

                # Alpha composite the transparent layer (with the overlay) onto the original image
                combined_image = Image.alpha_composite(original_image, transparent_layer)

                # Convert back to RGB if original was not RGBA (optional, depends on desired output format)
                # combined_image = combined_image.convert("RGB")

                # Save the modified image with the new name
                combined_image.save(new_file)
                print(f"Processed and saved: {new_file}")
            except Exception as img_e:
                 print(f"Error processing file {filename}: {img_e}")
        
        # עדכון סיום
        if status_label:
            status_label.config(text="העיבוד הושלם!")


    except FileNotFoundError:
        print(f"Error: Directory or overlay image not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_all_inputs():
    # טעינת הגדרות שמורות
    settings = load_settings()
    
    def browse_source():
        path = filedialog.askdirectory(title="בחר תיקיית מקור")
        if path:
            source_var.set(path)
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
        
        # בדיקת תקינות גודל וריווח
        try:
            width = int(width_var.get())
            height = int(height_var.get())
            margin_top = int(margin_top_var.get())
            margin_right = int(margin_right_var.get())
            
            if width <= 0 or height <= 0:
                result_label.config(text="גודל חייב להיות מספר חיובי", fg="red")
                return
            if margin_top < 0 or margin_right < 0:
                result_label.config(text="ריווח חייב להיות מספר לא שלילי", fg="red")
                return
        except ValueError:
            result_label.config(text="נא להזין מספרים תקינים", fg="red")
            return
        
        # שמירת הגדרות
        save_settings(overlay_var.get(), width, height, margin_top, margin_right)
        
        # הפעלת העיבוד
        process_images()
    
    def process_images():
        """פונקציה לעיבוד התמונות"""
        source_directory = source_var.get()
        destination_directory = dest_var.get()
        custom_name = custom_var.get()
        date = date_var.get()
        overlay_image_path = overlay_var.get()
        overlay_width = int(width_var.get())
        overlay_height = int(height_var.get())
        margin_top = int(margin_top_var.get())
        margin_right = int(margin_right_var.get())
        
        base_name = "ארכיון - תמונה מס' "
        
        # ספירת קבצים לעיבוד
        try:
            files = os.listdir(source_directory)
            image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
            total_files = len(image_files)
        except:
            total_files = 0
        
        if total_files > 0:
            # יצירת פונקציית callback לעיבוד
            def process_callback(progress_var, progress_bar, status_label, is_cancelled_func):
                rename_images(source_directory, destination_directory, base_name, custom_name, date, 
                            overlay_image_path, overlay_width, overlay_height, margin_top, margin_right, 
                            progress_var, progress_bar, status_label, is_cancelled_func)
            
            # הצגת חלון progress
            cancelled = show_progress_window(total_files, process_callback)
            
            if not cancelled:
                # הצגת הודעת סיום
                messagebox.showinfo("סיום", "העיבוד הושלם בהצלחה!")
            else:
                messagebox.showinfo("ביטול", "העיבוד בוטל על ידי המשתמש")
        else:
            messagebox.showerror("שגיאה", "לא נמצאו קבצי תמונה לעיבוד")
    
    root = Tk()
    root.title("הגדר נתונים")
    # משתנים
    source_var = StringVar()
    dest_var = StringVar()
    custom_var = StringVar()
    date_var = StringVar()
    overlay_var = StringVar(value=settings["overlay_path"])
    width_var = StringVar(value=str(settings["overlay_width"]))
    height_var = StringVar(value=str(settings["overlay_height"]))
    margin_top_var = StringVar(value=str(settings["margin_top"]))
    margin_right_var = StringVar(value=str(settings["margin_right"]))
    
    # שורות
    Label(root, text="תיקיית מקור:").grid(row=0, column=0, sticky='e')
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
    
    # שדות גודל
    Label(root, text="רוחב שכבת-על:").grid(row=5, column=0, sticky='e')
    Entry(root, textvariable=width_var, width=10).grid(row=5, column=1, sticky='w')
    Label(root, text="גובה שכבת-על:").grid(row=5, column=1, sticky='e', padx=(50,0))
    Entry(root, textvariable=height_var, width=10).grid(row=5, column=2, sticky='w')
    
    # שדות ריווח
    Label(root, text="ריווח מלמעלה:").grid(row=6, column=0, sticky='e')
    Entry(root, textvariable=margin_top_var, width=10).grid(row=6, column=1, sticky='w')
    Label(root, text="ריווח מימין:").grid(row=6, column=1, sticky='e', padx=(50,0))
    Entry(root, textvariable=margin_right_var, width=10).grid(row=6, column=2, sticky='w')
    
    result_label = Label(root, text="", fg="red")
    result_label.grid(row=7, column=0, columnspan=3)
    Button(root, text="אישור", command=submit).grid(row=8, column=0, columnspan=3)
    root.mainloop()
    # הפונקציה לא מחזירה ערכים כי החלון נשאר פתוח

# --- Main Execution ---
if __name__ == "__main__":
    # הפעלת החלון הראשי - הוא יישאר פתוח
    get_all_inputs()