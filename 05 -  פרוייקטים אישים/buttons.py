import tkinter as tk
import subprocess

def run_script(script_name):
    try:
        subprocess.run(["python", script_name])
    except Exception as e:
        print(f"Error running {script_name}: {e}")

class Buttons:
# יצירת חלון ראשי
    root = tk.Tk()
    root.title("תוכנה עם 3 כפתורים")
    root.geometry("300x200")

    # יצירת כפתורים
    button1 = tk.Button(root, text="הפעל סקריפט 1", command=lambda: run_script("script.py"))
    button2 = tk.Button(root, text="הפעל סקריפט 2", command=lambda: run_script("script2.py"))
    button3 = tk.Button(root, text="הפעל סקריפט 3", command=lambda: run_script("script3.py"))
    button4 = tk.Button(root, text = "stop",width=10, command=root.destroy)

    # מיקום הכפתורים
    button1.pack(pady=10)
    button2.pack(pady=10)
    button3.pack(pady=10)
    button4.pack(pady=10)

    # הפעלת הלולאה הראשית של tkinter
    root.mainloop()
