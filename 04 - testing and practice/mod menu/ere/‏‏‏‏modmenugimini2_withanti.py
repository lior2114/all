# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import ctypes
import sys
import win32gui
import win32con
import win32api
import win32process
import psutil
from PIL import Image, ImageTk, ImageFilter
import numpy as np
import cv2
import win32event
import threading
import base64
import os

def decrypt_string(encrypted_string):
    # Example decryption function (Base64 decoding for simplicity)
    return base64.b64decode(encrypted_string).decode('utf-8')

def is_running_in_vm():
    # Example VM detection logic
    vm_indicators = ["VBOX", "VMWARE", "VIRTUAL"]
    for indicator in vm_indicators:
        if indicator in os.popen('wmic baseboard get product,Manufacturer').read().upper():
            return True
    return False

def hide_window():
    # Hide the window from EnumWindows
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 0)  # 0 = SW_HIDE

# ============= כתובות בסיס להגדרה =============
# !!! חשוב: יש להחליף את הכתובות האלו בכתובות הזיכרון האמיתיות של המשחק שלך !!!
# מציאת כתובות אלו דורשת שימוש בכלים כמו Cheat Engine
BASE_ADDRESSES = {
    # נתונים של השחקן
    "health": 0x00000000,      # כתובת חיים
    "armor": 0x00000000,       # כתובת שריון
    "ammo": 0x00000000,        # כתובת תחמושת
    "money": 0x00000000,       # כתובת כסף
    "score": 0x00000000,       # כתובת ניקוד

    # כלי נשק
    "weapons": 0x00000000,     # כתובת רשימת הנשקים (יכול להיות מצביע או מבנה)
    "current_weapon": 0x00000000, # כתובת הנשק הנוכחי

    # תנועה
    "speed": 0x00000000,       # כתובת מהירות תנועה
    "jump": 0x00000000,        # כתובת גובה קפיצה

    # שונות
    "god_mode": 0x00000000,    # כתובת מצב אלוהים (God Mode)
    "no_clip": 0x00000000,     # כתובת No Clip (מעבר דרך קירות)
    "invisibility": 0x00000000 # כתובת אי-נראות
}

# ============= רשימת כלי נשק =============
# !!! חשוב: יש להתאים את השמות והערכים למשחק הספציפי !!!
# הערכים יכולים להיות ID של נשק, אופסט, או ערך אחר בהתאם למשחק
WEAPONS = {
    "Pistol": 0x00000001,
    "Shotgun": 0x00000002,
    "SMG": 0x00000003,
    "Rifle": 0x00000004,
    "Sniper": 0x00000005,
    "RPG": 0x00000006,
    "Grenade": 0x00000007,
    "Knife": 0x00000008
}

# ============= קטגוריות פיצ'רים לתצוגה =============
# מארגן את הפיצ'רים מ-BASE_ADDRESSES לקטגוריות עבור הטאבים ב-GUI
FEATURE_CATEGORIES = {
    "נתוני שחקן": {
        "health": "חיים ללא הגבלה",
        "armor": "שריון ללא הגבלה",
        "ammo": "תחמושת ללא הגבלה",
        "money": "כסף ללא הגבלה",
        "score": "ניקוד מקסימלי"
    },
    "כלי נשק": {
        "weapons": "פתיחת כל הנשקים", # הערה: מימוש זה יכול להיות מורכב
        "current_weapon": "החלפת נשק נוכחי" # הערה: ייתכן ויצריך מימוש נוסף
    },
    "תנועה": {
        "speed": "פריצת מהירות (Speed Hack)",
        "jump": "קפיצת על (Super Jump)",
        "no_clip": "מעבר דרך קירות (No Clip)"
    },
    "שונות": {
        "god_mode": "מצב אלוהים (God Mode)",
        "invisibility": "אי-נראות (Invisibility)"
    }
}

# קלאס ליצירת רקע מטושטש דינמי
class BlurredBackground(tk.Canvas):
    def __init__(self, parent, blur_amount=5):
        super().__init__(parent)
        self.blur_amount = blur_amount
        # קושרים את שינוי גודל החלון לפונקציה שמעדכנת את הרקע
        self.bind('<Configure>', self._on_resize)
        self.background = None # אתחול המשתנה

    def _on_resize(self, event):
        # יצירת תמונה חדשה בגודל החלון הנוכחי
        width = event.width
        height = event.height

        if width <= 0 or height <= 0: # בדיקה למניעת שגיאות בגודל 0
             return

        # יצירת רקע עם גרדיאנט (מעבר צבעים) אפור כהה
        image = np.zeros((height, width, 3), dtype=np.uint8)
        for i in range(height):
            # צבע משתנה מאפור כהה (למעלה) לאפור כהה יותר (למטה)
            color_value = int(50 * (1 - i / height)) # טווח 0-50 כהה
            image[i, :] = [color_value, color_value, color_value] # גווני אפור

        # החלת טשטוש גאוסיאני באמצעות OpenCV
        # גודל הגרעין חייב להיות אי-זוגי וחיובי
        kernel_size = self.blur_amount * 2 + 1
        try:
            blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
        except cv2.error: # תופס שגיאה אפשרית אם הגרעין לא תקין
            blurred = image # אם יש בעיה, מציגים את התמונה המקורית

        # המרת המערך של numpy לתמונה של PIL ואז ל-PhotoImage של Tkinter
        self.background = ImageTk.PhotoImage(image=Image.fromarray(blurred))

        # עדכון הקנבס: מחיקת הרקע הישן והצגת החדש
        self.delete("background")
        self.create_image(0, 0, image=self.background, anchor="nw", tags="background")
        # הורדת תג הרקע לשכבה התחתונה
        self.tag_lower("background")

# קלאס ראשי של תפריט המודים
class EnhancedModMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ZSCY Mod Menu")
        self.root.geometry("900x700") # גודל חלון התחלתי

        # אתחול משתני מצב ומילונים
        self.selected_process = None # לא נבחר תהליך בהתחלה
        self.process_handle = None # Handle לתהליך הנבחר
        # מילון לשמירת מצב (פועל/כבוי) של כל פיצ'ר
        self.feature_states = {feature: False for feature in BASE_ADDRESSES.keys()}
        # מילון לשמירת הכפתורים של הפיצ'רים (כדי לשנות את צבעם)
        self.feature_buttons = {}

        # יצירת הרקע המטושטש
        self.background = BlurredBackground(self.root, blur_amount=10) # הגדלת הטשטוש
        self.background.pack(fill='both', expand=True)

        # יצירת מסגרת ראשית (שקופה למחצה על הרקע)
        # שים לב: Tkinter לא תומך בשקיפות אמיתית בקלות. הרקע של המסגרת פשוט יסתיר את הקנבס מתחתיו.
        # צבע הרקע של המסגרת צריך להיות כהה כדי להשתלב.
        self.main_frame = tk.Frame(self.background, bg='#1a1a1a')
        # ממקמים את המסגרת במרכז החלון
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center', width=600, height=550) # גודל קבוע למסגרת

        # כותרת מעוצבת
        title_label = tk.Label(
            self.main_frame,
            text="ZSCY",
            font=("Arial", 30, "bold"), # הגדלת הפונט
            fg="#00ff00", # צבע ירוק זוהר
            bg='#1a1a1a'  # רקע שיתאים למסגרת
        )
        title_label.pack(pady=20)

        # מסגרת לבחירת תהליך
        self.process_frame = tk.Frame(self.main_frame, bg='#1a1a1a')
        self.process_frame.pack(fill='x', pady=10, padx=20)

        # כפתור לבחירת תהליך המשחק
        self.process_btn = self.create_button("בחר תהליך משחק", self.select_process, parent=self.process_frame, width=20)
        self.process_btn.pack(side='left', padx=10) # מיקום בצד שמאל

        # תווית להצגת התהליך שנבחר
        self.process_label = tk.Label(
            self.process_frame,
            text="לא נבחר תהליך",
            fg="#ff0000", # צבע אדום כשאין בחירה
            bg='#1a1a1a',
            font=("Arial", 10)
        )
        self.process_label.pack(side='left', padx=10) # מיקום לצד הכפתור

        # יצירת טאבים (לשוניות) לקטגוריות
        self.create_category_tabs()

        # בדיקה אם החלון צריך להיות תמיד למעלה (אופציונלי)
        # self.root.attributes('-topmost', True)

        # טיפול בסגירת החלון - לשחרר את ה-handle של התהליך
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    # פונקציה ליצירת כפתורים מעוצבים
    def create_button(self, text, command, parent=None, width=18): # הגדלת רוחב ברירת מחדל
        if parent is None:
            parent = self.main_frame

        btn = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Arial", 10),
            bg='#333333', # רקע אפור כהה
            fg='white',   # טקסט לבן
            activebackground='#00cc00', # רקע ירוק בהיר יותר בלחיצה
            activeforeground='black', # טקסט שחור בלחיצה
            relief=tk.FLAT, # ללא מסגרת בולטת
            width=width,   # רוחב הכפתור
            pady=4 # ריווח פנימי אנכי
        )
        # שינוי צבע הרקע כשעוברים עם העכבר
        btn.bind("<Enter>", lambda e: btn.config(bg='#444444'))
        btn.bind("<Leave>", lambda e: btn.config(bg='#333333' if not self.is_feature_active(btn) else '#00ff00'))

        btn.pack(pady=4, padx=10, fill='x') # ריווח חיצוני ומילוי אופקי
        return btn

    # פונקציה לבדוק אם הכפתור מייצג פיצ'ר פעיל
    def is_feature_active(self, btn):
         # נמצא את מזהה הפיצ'ר המשויך לכפתור הזה
         for feature_id, button in self.feature_buttons.items():
              if button == btn:
                   return self.feature_states.get(feature_id, False)
         return False # אם לא נמצא פיצ'ר משויך

    # פונקציה ליצירת הטאבים והכפתורים בתוכם
    def create_category_tabs(self):
        # יצירת אזור הטאבים (Notebook)
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill='both', expand=True, padx=20, pady=20)

        # הגדרת סגנון עיצובי לטאבים
        style = ttk.Style()
        style.theme_use('clam') # ערכת נושא מודרנית יותר
        style.configure("TNotebook", background='#1a1a1a', borderwidth=0)
        style.configure("TNotebook.Tab", background='#333333', foreground='white', padding=[10, 5], font=('Arial', 10))
        # שינוי צבע הטאב הנבחר
        style.map("TNotebook.Tab", background=[("selected", "#00ff00")], foreground=[("selected", "black")])

        # יצירת טאב לכל קטגוריה מהמילון
        for category_name, features in FEATURE_CATEGORIES.items():
            tab = tk.Frame(self.notebook, bg='#1a1a1a')
            self.notebook.add(tab, text=category_name)

            # יצירת כפתורים להפעלת/כיבוי הפיצ'רים בקטגוריה זו
            for feature_id, feature_name in features.items():
                 # בודקים אם הפיצ'ר קיים ב-BASE_ADDRESSES לפני יצירת הכפתור
                 if feature_id in BASE_ADDRESSES:
                    # lambda f=feature_id: ... יוצר פונקציה נפרדת לכל כפתור עם ה-ID הנכון
                    btn = self.create_button(feature_name, lambda f=feature_id: self.toggle_feature(f), tab)
                    # שמירת הכפתור במילון כדי שנוכל לשנות את צבעו מאוחר יותר
                    self.feature_buttons[feature_id] = btn

            # טיפול מיוחד בטאב "כלי נשק" - הוספת כפתורים לנשקים ספציפיים
            if category_name == "כלי נשק":
                # הוספת קו הפרדה
                separator = tk.Frame(tab, height=2, bg='#333333')
                separator.pack(fill='x', pady=10, padx=5)

                # הוספת תווית הסבר
                weapon_label = tk.Label(
                    tab,
                    text="הוספת נשקים בודדים:",
                    font=("Arial", 12, "bold"),
                    fg="#00ff00",
                    bg='#1a1a1a'
                )
                weapon_label.pack(pady=5)

                # יצירת כפתורים להוספת כל נשק מהרשימה
                weapon_frame = tk.Frame(tab, bg='#1a1a1a') # מסגרת לכפתורי הנשקים
                weapon_frame.pack(fill='x')
                col = 0
                for weapon_name in WEAPONS.keys():
                     btn = self.create_button(f"הוסף {weapon_name}", lambda w=weapon_name: self.add_weapon(w), weapon_frame, width=12)
                     btn.pack(side=tk.LEFT, padx=5, pady=5, expand=True) # סידור הכפתורים בשורה
                     col += 1
                     if col % 3 == 0: # ירידת שורה כל 3 כפתורים (בערך)
                          weapon_frame = tk.Frame(tab, bg='#1a1a1a')
                          weapon_frame.pack(fill='x')


    # פונקציה להפעלת/כיבוי פיצ'ר
    def toggle_feature(self, feature):
        # בדיקה אם נבחר תהליך משחק
        if not self.selected_process or not self.process_handle:
            messagebox.showerror("שגיאה", "אנא בחר תהליך משחק תחילה!")
            return

        # בדיקה אם הפיצ'ר קיים בכתובות הבסיס
        if feature not in BASE_ADDRESSES:
            messagebox.showerror("שגיאה", f"הפיצ'ר '{feature}' אינו מוגדר כראוי.")
            return

        try:
            address = BASE_ADDRESSES[feature]
            current_state = self.feature_states[feature]
            new_state = not current_state

            # כאן צריך לבוא הקוד שמשנה את הזיכרון בפועל
            # ==================================================
            # !!! קוד לשינוי זיכרון חסר !!!
            # דוגמה (תיאורטית, דורשת מימוש נכון עם pywin32/ctypes):
            # value_to_write = 1 if new_state else 0 # או ערך אחר בהתאם למשחק
            # write_memory(self.process_handle, address, value_to_write, data_type)
            print(f"Attempting to toggle '{feature}' at address {hex(address)} to state {new_state}")
            # ==================================================

            # אם שינוי הזיכרון (ההיפותטי) הצליח:
            self.feature_states[feature] = new_state # עדכון המצב הפנימי
            button = self.feature_buttons.get(feature) # קבלת הכפתור מהמילון
            if button:
                 if new_state:
                      # שינוי צבע הכפתור למצב 'פועל'
                      button.config(bg='#00ff00', fg='black', activebackground='#00cc00')
                      # עדכון מצב העכבר אם הוא מעל הכפתור
                      if button.winfo_containing(button.winfo_pointerx(), button.winfo_pointery()) == button:
                           button.config(bg='#00cc00')
                 else:
                      # שינוי צבע הכפתור למצב 'כבוי'
                      button.config(bg='#333333', fg='white', activebackground='#00cc00')
                      # עדכון מצב העכבר אם הוא מעל הכפתור
                      if button.winfo_containing(button.winfo_pointerx(), button.winfo_pointery()) == button:
                           button.config(bg='#444444')


            status_text = "מופעל" if new_state else "מבוטל"
            feature_name_heb = FEATURE_CATEGORIES.get(self.get_category_from_feature(feature), {}).get(feature, feature.replace('_', ' ').title())
            messagebox.showinfo("הצלחה", f"{feature_name_heb} {status_text}!")

        except Exception as e:
            # הדפסת השגיאה המלאה לקונסול לצורך דיבאג
            print(f"Error toggling feature '{feature}': {e}")
            import traceback
            traceback.print_exc()
            messagebox.showerror("שגיאה", f"נכשל בשינוי מצב של {feature}: {str(e)}\nייתכן שאין הרשאות או שהכתובת שגויה.")

    # פונקציית עזר למצוא את שם הקטגוריה לפי מזהה הפיצ'ר
    def get_category_from_feature(self, feature_id):
        for category, features in FEATURE_CATEGORIES.items():
            if feature_id in features:
                return category
        return None

    # פונקציה להוספת נשק
    def add_weapon(self, weapon_name):
        if not self.selected_process or not self.process_handle:
            messagebox.showerror("שגיאה", "אנא בחר תהליך משחק תחילה!")
            return

        if weapon_name not in WEAPONS:
             messagebox.showerror("שגיאה", f"הנשק '{weapon_name}' אינו מוגדר.")
             return

        try:
            weapon_id = WEAPONS[weapon_name]
            # כאן צריך לבוא הקוד שמוסיף את הנשק במשחק
            # זה יכול להיות מורכב ותלוי איך המשחק מנהל את הנשקים
            # (למשל: כתיבה למערך נשקים, קריאה לפונקציה במשחק וכו')
            # ==================================================
            # !!! קוד להוספת נשק חסר !!!
            # דוגמה תיאורטית:
            # weapon_list_address = BASE_ADDRESSES.get("weapons")
            # if weapon_list_address:
            #     add_weapon_to_memory(self.process_handle, weapon_list_address, weapon_id)
            print(f"Attempting to add weapon '{weapon_name}' (ID: {hex(weapon_id)})")
            # ==================================================

            messagebox.showinfo("הצלחה", f"הנשק {weapon_name} נוסף (תיאורטית)!")
        except Exception as e:
            print(f"Error adding weapon '{weapon_name}': {e}")
            import traceback
            traceback.print_exc()
            messagebox.showerror("שגיאה", f"נכשל בהוספת הנשק {weapon_name}: {str(e)}")

    # פונקציה לפתיחת חלון בחירת תהליך
    def select_process(self):
        try:
            # קבלת רשימת תהליכים רצים באמצעות psutil
            processes = []
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    # שמירת שם ו-PID של כל תהליך
                    processes.append((proc.info['name'], proc.info['pid']))
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    # התעלמות מתהליכים שאין אליהם גישה או שכבר לא קיימים
                    pass

            # יצירת חלון חדש (Toplevel) לבחירת תהליך
            process_window = tk.Toplevel(self.root)
            process_window.title("בחר תהליך משחק")
            process_window.geometry("450x550") # הגדלת החלון
            process_window.configure(bg='#1a1a1a')
            process_window.attributes('-topmost', True) # חלון תמיד למעלה

            # מסגרת לשדה החיפוש
            search_frame = tk.Frame(process_window, bg='#1a1a1a')
            search_frame.pack(fill='x', padx=10, pady=10)

            # תווית לשדה החיפוש
            search_label = tk.Label(search_frame, text="חיפוש:", font=("Arial", 10), fg="white", bg='#1a1a1a')
            search_label.pack(side='left', padx=5)

            # שדה קלט (Entry) לחיפוש
            search_var = tk.StringVar()
            search_entry = tk.Entry(search_frame, textvariable=search_var, font=("Arial", 10), bg='#333333', fg='white', insertbackground='white') # insertbackground = צבע הסמן
            search_entry.pack(side='left', fill='x', expand=True, padx=5)
            search_entry.focus() # מיקוד אוטומטי בשדה החיפוש

            # מסגרת לרשימה ולפס הגלילה
            frame = tk.Frame(process_window, bg='#1a1a1a')
            frame.pack(fill='both', expand=True, padx=10, pady=5)

            # פס גלילה אנכי
            scrollbar = tk.Scrollbar(frame)
            scrollbar.pack(side='right', fill='y')

            # תיבת רשימה (Listbox) להצגת התהליכים
            listbox = tk.Listbox(
                frame,
                bg='#333333',
                fg='white',
                selectmode='single', # אפשרות בחירה יחידה
                yscrollcommand=scrollbar.set, # קישור לפס הגלילה
                font=("Arial", 10),
                selectbackground="#00ff00", # צבע רקע לפריט שנבחר
                selectforeground="black"  # צבע טקסט לפריט שנבחר
            )
            listbox.pack(side='left', fill='both', expand=True)

            # קישור פס הגלילה לפעולת הגלילה של הרשימה
            scrollbar.config(command=listbox.yview)

            # מיון התהליכים לפי שם (אופציונלי)
            processes.sort(key=lambda x: x[0].lower())

            # הוספת התהליכים לרשימה
            for proc_name, proc_pid in processes:
                listbox.insert('end', f"{proc_name} (PID: {proc_pid})")

            # שמירת רשימת כל התהליכים לשימוש בסינון
            all_processes = processes.copy()

            # פונקציה פנימית לסינון הרשימה לפי החיפוש
            def filter_processes(*args):
                search_term = search_var.get().lower()
                listbox.delete(0, tk.END) # מחיקת כל הפריטים הנוכחיים

                # מעבר על כל התהליכים המקוריים והוספה מחדש של המתאימים
                for proc_name, proc_pid in all_processes:
                    if search_term in proc_name.lower():
                        listbox.insert('end', f"{proc_name} (PID: {proc_pid})")

            # קישור האירוע 'שינוי בשדה החיפוש' לפונקציית הסינון
            search_var.trace('w', filter_processes)

            # פונקציה פנימית שמופעלת בעת בחירת תהליך מהרשימה
            def on_select(event=None): # הוספת event כדי שנוכל לקשור גם ללחיצה כפולה
                if not listbox.curselection(): # בדיקה אם נבחר משהו
                    return

                selected_index = listbox.curselection()[0]
                selected_text = listbox.get(selected_index)

                # חילוץ ה-PID מהטקסט שנבחר
                try:
                    # "ProcessName (PID: 1234)" -> 1234
                    pid_str = selected_text.split('PID: ')[1].replace(')', '')
                    proc_pid = int(pid_str)
                    proc_name = selected_text.split(' (PID:')[0]

                    # ניסיון לפתוח את התהליך ולקבל handle
                    try:
                         # בקשת כל ההרשאות האפשריות - דורש הרשאות מנהל
                         self.process_handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, proc_pid)
                         self.selected_process = proc_pid # שמירת ה-PID
                         # עדכון התווית בחלון הראשי
                         self.process_label.config(text=f"נבחר: {proc_name} (PID: {proc_pid})", fg="#00ff00")
                         process_window.destroy() # סגירת חלון הבחירה
                         messagebox.showinfo("הצלחה", f"התהליך '{proc_name}' נבחר בהצלחה.")

                    except Exception as open_error:
                         # אם נכשל בפתיחת התהליך (לרוב בגלל הרשאות)
                         print(f"Error opening process {proc_pid}: {open_error}")
                         messagebox.showerror("שגיאה בפתיחת תהליך", f"לא ניתן לפתוח את התהליך {proc_name} (PID: {proc_pid}).\nודא שהתוכנה רצה כמנהל ושלתהליך יש הרשאות מתאימות.\nשגיאה: {open_error}")
                         self.process_handle = None
                         self.selected_process = None
                         self.process_label.config(text="בחירת תהליך נכשלה", fg="#ff0000")

                except (IndexError, ValueError) as parse_error:
                    # אם היה כשל בחילוץ ה-PID מהטקסט
                     print(f"Error parsing selected process string '{selected_text}': {parse_error}")
                     messagebox.showerror("שגיאה", "שגיאה בעיבוד בחירת התהליך.")


            # קשירת לחיצה כפולה על פריט ברשימה לפונקציית הבחירה
            listbox.bind("<Double-Button-1>", on_select)

            # מסגרת לכפתורי הבחירה והביטול
            button_frame = tk.Frame(process_window, bg='#1a1a1a')
            button_frame.pack(fill='x', padx=10, pady=10)

            # כפתור "בחר"
            select_btn = tk.Button(button_frame, text="בחר", command=on_select, font=("Arial", 10), bg='#333333', fg='white', activebackground='#00ff00', activeforeground='black', relief=tk.FLAT, width=10)
            select_btn.pack(side='right', padx=5)

            # כפתור "בטל"
            cancel_btn = tk.Button(button_frame, text="בטל", command=process_window.destroy, font=("Arial", 10), bg='#333333', fg='white', activebackground='#ff0000', activeforeground='black', relief=tk.FLAT, width=10)
            cancel_btn.pack(side='right', padx=5)

        except Exception as e:
             print(f"Error getting process list: {e}")
             import traceback
             traceback.print_exc()
             messagebox.showerror("שגיאה", f"נכשל בקבלת רשימת התהליכים: {str(e)}")

    # פונקציה להזרקת DLL (כרגע לא בשימוש פעיל בקוד)
    def inject_dll(self, process_id):
        try:
            # קבלת handle לתהליך (אם עדיין אין)
            process_handle_local = self.process_handle
            if not process_handle_local and process_id == self.selected_process:
                 # אם מנסים להזריק לתהליך הנבחר ואין handle, ננסה לפתוח
                 try:
                      process_handle_local = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, process_id)
                 except Exception as open_error:
                      raise Exception(f"Failed to open process {process_id} for injection: {open_error}") from open_error
            elif not process_handle_local:
                 # אם מנסים להזריק לתהליך אחר שאינו הנבחר, חייבים לפתוח אותו
                 try:
                      process_handle_local = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, process_id)
                 except Exception as open_error:
                      raise Exception(f"Failed to open process {process_id} for injection: {open_error}") from open_error


            # !!! חשוב: החלף את הנתיב בנתיב האמיתי לקובץ ה-DLL שלך !!!
            dll_path = r"C:\path\to\your\actual\cheat.dll" # שימוש ב-raw string (r"...") עדיף לנתיבים
            # בדיקה אם הקובץ קיים לפני שמנסים להזריק
            if not os.path.exists(dll_path):
                 raise FileNotFoundError(f"DLL file not found at: {dll_path}")


            # המרת נתיב ה-DLL ל-bytes עם תו null בסוף
            path_bytes = (dll_path + '\0').encode('utf-8')
            path_size = len(path_bytes)

            # הקצאת זיכרון בתהליך המטרה עבור נתיב ה-DLL
            remote_memory = win32process.VirtualAllocEx(
                process_handle_local,
                0, # כתובת רצויה (0 = המערכת תחליט)
                path_size, # גודל הזיכרון להקצאה
                win32con.MEM_COMMIT | win32con.MEM_RESERVE, # סוג ההקצאה
                win32con.PAGE_READWRITE # הרשאות גישה לזיכרון שהוקצה
            )
            if not remote_memory: # בדיקה אם ההקצאה הצליחה
                 raise Exception(f"Failed to allocate memory in target process. Error code: {win32api.GetLastError()}")

            # כתיבת נתיב ה-DLL לזיכרון שהוקצה בתהליך המטרה
            bytes_written = win32process.WriteProcessMemory(
                process_handle_local,
                remote_memory, # הכתובת שהתקבלה מ-VirtualAllocEx
                path_bytes,    # ה-bytes של הנתיב
                path_size      # גודל הנתונים לכתיבה
            )
            # WriteProcessMemory מחזירה bool, לא מספר בתים ב-pywin32 הישן
            # if bytes_written != path_size: # בדיקה אם הכתיבה הצליחה במלואה
            #     win32process.VirtualFreeEx(process_handle_local, remote_memory, 0, win32con.MEM_RELEASE) # שחרור הזיכרון במקרה של כישלון
            #     raise Exception(f"Failed to write DLL path to target process memory. Wrote {bytes_written}/{path_size} bytes. Error code: {win32api.GetLastError()}")
            # בדיקה פשוטה יותר אם הכתיבה הצליחה
            if not bytes_written:
                win32process.VirtualFreeEx(process_handle_local, remote_memory, 0, win32con.MEM_RELEASE)
                raise Exception(f"Failed to write DLL path to target process memory. Error code: {win32api.GetLastError()}")


            # קבלת כתובת הפונקציה LoadLibraryA מתוך kernel32.dll
            # kernel32.dll נטען תמיד לתוך כל תהליך, והכתובת של LoadLibraryA זהה בדרך כלל
            kernel32 = win32api.GetModuleHandle('kernel32.dll')
            load_library_addr = win32api.GetProcAddress(kernel32, 'LoadLibraryA')
            if not load_library_addr:
                 win32process.VirtualFreeEx(process_handle_local, remote_memory, 0, win32con.MEM_RELEASE)
                 raise Exception(f"Failed to get address of LoadLibraryA. Error code: {win32api.GetLastError()}")


            # יצירת תהליכון (thread) מרוחק בתהליך המטרה
            # התהליכון יתחיל מהכתובת של LoadLibraryA ויקבל כפרמטר את הכתובת של נתיב ה-DLL שהקצנו
            thread_handle, thread_id = win32process.CreateRemoteThread(
                process_handle_local, # Handle לתהליך המטרה
                None,           # אבטחה (ברירת מחדל)
                0,              # גודל המחסנית (ברירת מחדל)
                load_library_addr, # כתובת הפונקציה להתחלה (LoadLibraryA)
                remote_memory,  # פרמטר לפונקציה (הכתובת של נתיב ה-DLL)
                0,              # דגלי יצירה (0 = התחל מיד)
                None            # קבלת ID של התהליכון (לא נחוץ כאן)
            )
            if not thread_handle:
                 win32process.VirtualFreeEx(process_handle_local, remote_memory, 0, win32con.MEM_RELEASE)
                 raise Exception(f"Failed to create remote thread. Error code: {win32api.GetLastError()}")

            # המתנה לסיום התהליכון (כלומר, עד ש-LoadLibraryA יסיים לטעון את ה-DLL)
            win32event.WaitForSingleObject(thread_handle, win32event.INFINITE) # INFINITE = המתן ללא הגבלת זמן

            # ניקוי וסגירת Handles ושחרור הזיכרון
            win32api.CloseHandle(thread_handle)
            win32process.VirtualFreeEx(process_handle_local, remote_memory, 0, win32con.MEM_RELEASE)
            # לא לסגור את ה-handle הראשי כאן אם הוא שייך למחלקה
            if process_handle_local != self.process_handle:
                 win32api.CloseHandle(process_handle_local)

            messagebox.showinfo("הצלחה", "DLL הוזרק בהצלחה!")
            return True

        except FileNotFoundError as fnf_error:
             messagebox.showerror("שגיאה בהזרקת DLL", str(fnf_error))
             return False
        except Exception as e:
            print(f"Error injecting DLL: {e}")
            import traceback
            traceback.print_exc()
            # ננסה לסגור handles פתוחים במקרה של שגיאה באמצע
            if 'thread_handle' in locals() and thread_handle: win32api.CloseHandle(thread_handle)
            if 'remote_memory' in locals() and remote_memory and 'process_handle_local' in locals() and process_handle_local:
                 try: win32process.VirtualFreeEx(process_handle_local, remote_memory, 0, win32con.MEM_RELEASE)
                 except: pass # אם השחרור נכשל, אין הרבה מה לעשות
            if 'process_handle_local' in locals() and process_handle_local and process_handle_local != self.process_handle:
                 try: win32api.CloseHandle(process_handle_local)
                 except: pass

            messagebox.showerror("שגיאה בהזרקת DLL", f"נכשל בהזרקת DLL: {str(e)}")
            return False

    # פונקציה המופעלת לפני סגירת החלון
    def on_closing(self):
         print("Closing application and releasing process handle...")
         # שחרור ה-handle של התהליך אם הוא קיים
         if self.process_handle:
              try:
                   win32api.CloseHandle(self.process_handle)
                   self.process_handle = None
                   self.selected_process = None
              except Exception as e:
                   print(f"Error closing process handle: {e}")
         # סגירת חלון ה-Tkinter
         self.root.destroy()


    # פונקציה להרצת הלולאה הראשית של Tkinter
    def run(self):
        # Run the main loop directly in the main thread
        self.root.mainloop()

# נקודת הכניסה הראשית של התוכנה
if __name__ == "__main__":
    # בדיקה אם התוכנה רצה עם הרשאות מנהל (חשוב לגישה לזיכרון של תהליכים אחרים)
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        # אם יש בעיה בגישה ל-ctypes (נדיר), נניח שאין הרשאות
        is_admin = False
        print("Could not determine admin status using ctypes.")

    if not is_admin:
        print("This program requires administrator privileges.")
        sys.exit(1)

    if is_running_in_vm():
        print("Running in a virtual machine. Exiting.")
        sys.exit(1)

    hide_window()

    # Example encrypted payload (Base64 encoded string)
    encrypted_payload = "U29tZSBlbmNyeXB0ZWQgcGF5bG9hZA=="  # "Some encrypted payload"
    decrypted_payload = decrypt_string(encrypted_payload)
    print(f"Decrypted payload: {decrypted_payload}")

    # יצירת מופע של תפריט המודים והפעלתו
    menu = EnhancedModMenu()
    menu.run()