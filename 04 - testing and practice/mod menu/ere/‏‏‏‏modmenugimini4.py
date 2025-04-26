# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import ctypes
from ctypes import wintypes
import sys
import win32gui
import win32con
import win32api
import win32process
import psutil
from PIL import Image, ImageTk
# Removed ImageFilter and numpy/cv2 dependencies for simplicity,
# using a simpler background. Replace if dynamic blur is essential.
# import numpy as np
# import cv2
import win32event
import threading
import base64
import os
import queue # For thread-safe GUI updates

# ============= קבועים והגדרות =============
PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_OPERATION = 0x0008
PROCESS_VM_READ = 0x0010
PROCESS_VM_WRITE = 0x0020
PROCESS_CREATE_THREAD = 0x0002

# הרשאות נדרשות - שילוב של כל מה שאנחנו צריכים
REQUIRED_ACCESS = (
    PROCESS_QUERY_INFORMATION | PROCESS_VM_OPERATION |
    PROCESS_VM_READ | PROCESS_VM_WRITE | PROCESS_CREATE_THREAD
)

# !!! חשוב: שנה לשם המודול הראשי של המשחק (לרוב שם קובץ ה-EXE) !!!
GAME_MODULE_NAME = "game.exe" # לדוגמה: "ac_client.exe", "hl2.exe"

# ============= כתובות אופסט (Offsets) להגדרה =============
# !!! חשוב: החלף את הכתובות האלו באופסטים (Offsets) האמיתיים מהמשחק שלך,
# יחסית לכתובת הבסיס של המודול שהוגדר ב-GAME_MODULE_NAME.
# מציאת אופסטים אלו דורשת שימוש בכלים כמו Cheat Engine.
# אלו *לא* כתובות אבסולוטיות!
BASE_OFFSETS = {
    # נתונים של השחקן (דוגמאות - חייבים להיות offsets אמיתיים)
    "health": 0x00109B74,      # Offset חיים (דוגמה)
    "armor": 0x00109B78,       # Offset שריון (דוגמה)
    "ammo": 0x00109B80,        # Offset תחמושת (דוגמה)
    "money": 0x00109F78,       # Offset כסף (דוגמה)
    "score": 0x0010A000,       # Offset ניקוד (דוגמה)

    # כלי נשק
    "weapons_struct_ptr": 0x00109B84, # Offset למצביע למבנה הנשקים (דוגמה)
    "current_weapon_id": 0x00109B88, # Offset למזהה הנשק הנוכחי (דוגמה)

    # תנועה
    "speed": 0x00109C00,       # Offset מהירות תנועה (דוגמה)
    "jump": 0x00109C04,        # Offset גובה קפיצה (דוגמה)

    # שונות
    "god_mode_flag": 0x0010A123, # Offset לדגל מצב אלוהים (דוגמה)
    "no_clip_flag": 0x0010A456,  # Offset לדגל No Clip (דוגמה)
    "invisibility_flag": 0x0010A789 # Offset לדגל אי-נראות (דוגמה)
}

# ============= רשימת כלי נשק =============
# !!! חשוב: יש להתאים את השמות וה-IDs למשחק הספציפי !!!
WEAPONS = {
    # IDs לדוגמה
    "Pistol": 1,
    "Shotgun": 2,
    "SMG": 3,
    "Rifle": 4,
    "Sniper": 5,
    "RPG": 6,
    "Grenade": 7,
    "Knife": 8
}

# ============= קטגוריות פיצ'רים לתצוגה =============
FEATURE_CATEGORIES = {
    "נתוני שחקן": {
        "health": "חיים (לפי ערך)", # שנה לערך ספציפי או toggle
        "armor": "שריון (לפי ערך)",
        "ammo": "תחמושת ללא הגבלה (Toggle)", # דוגמה ל-Toggle
        "money": "כסף (לפי ערך)",
        "score": "ניקוד (לפי ערך)"
    },
    "כלי נשק": {
        # "weapons_struct_ptr": "פתיחת כל הנשקים (מורכב)", # מצריך לוגיקה מורכבת
        "current_weapon_id": "החלף לנשק הבא (דוגמה)" # או בחירה ספציפית
    },
    "תנועה": {
        "speed": "פריצת מהירות (לפי ערך)",
        "jump": "קפיצת על (לפי ערך)",
        "no_clip_flag": "מעבר דרך קירות (Toggle)"
    },
    "שונות": {
        "god_mode_flag": "מצב אלוהים (Toggle)",
        "invisibility_flag": "אי-נראות (Toggle)"
    }
}

# --- פונקציות עזר לקריאה/כתיבה בזיכרון ---
def read_memory(process_handle, address, data_type, size):
    """קורא זיכרון מכתובת ספציפית."""
    if not process_handle or not address:
        # print("Read Error: Invalid handle or address.")
        return None
    buffer = ctypes.create_string_buffer(size)
    bytes_read = ctypes.c_size_t()
    try:
        if win32process.ReadProcessMemory(process_handle, address, buffer, size, ctypes.byref(bytes_read)):
            if bytes_read.value == size:
                if data_type == int:
                    if size == 4: return ctypes.cast(buffer, ctypes.POINTER(wintypes.DWORD))[0]
                    if size == 8: return ctypes.cast(buffer, ctypes.POINTER(ctypes.c_ulonglong))[0]
                    if size == 2: return ctypes.cast(buffer, ctypes.POINTER(wintypes.WORD))[0]
                    if size == 1: return ctypes.cast(buffer, ctypes.POINTER(wintypes.BYTE))[0]
                elif data_type == float:
                    if size == 4: return ctypes.cast(buffer, ctypes.POINTER(ctypes.c_float))[0]
                    if size == 8: return ctypes.cast(buffer, ctypes.POINTER(ctypes.c_double))[0]
                elif data_type == bytes:
                    return buffer.raw[:bytes_read.value]
                # Add other types (string with encoding, etc.) if needed
                print(f"Read Warning: Unsupported data type/size combination: {data_type}/{size}")
                return buffer.raw[:bytes_read.value] # Return raw bytes as fallback
            else:
                # print(f"Read Error: Read {bytes_read.value}/{size} bytes at {hex(address)}. Error: {win32api.GetLastError()}")
                return None
        else:
            # print(f"Failed to read memory at {hex(address)}. Error: {win32api.GetLastError()}")
            return None
    except Exception as e:
        print(f"Exception during read_memory at {hex(address)}: {e}")
        return None

def write_memory(process_handle, address, value, data_type, size):
    """כותב זיכרון לכתובת ספציפית."""
    if not process_handle or not address:
        # print("Write Error: Invalid handle or address.")
        return False
    c_value = None
    try:
        if data_type == int:
            if size == 4: c_value = wintypes.DWORD(value)
            elif size == 8: c_value = ctypes.c_ulonglong(value)
            elif size == 2: c_value = wintypes.WORD(value)
            elif size == 1: c_value = wintypes.BYTE(value)
        elif data_type == float:
            if size == 4: c_value = ctypes.c_float(value)
            elif size == 8: c_value = ctypes.c_double(value)
        elif data_type == bytes:
             if isinstance(value, bytes):
                 c_value = ctypes.create_string_buffer(value, size)
             else:
                 print("Write Error: Value must be bytes for data_type 'bytes'")
                 return False
        # Add other types if needed

        if c_value is None:
            print(f"Write Error: Unsupported data type/size combination for writing: {data_type}/{size}")
            return False

        bytes_written = ctypes.c_size_t()
        if win32process.WriteProcessMemory(process_handle, address, ctypes.byref(c_value), size, ctypes.byref(bytes_written)):
            if bytes_written.value == size:
                return True
            else:
                # print(f"Write Error: Wrote {bytes_written.value}/{size} bytes at {hex(address)}. Error: {win32api.GetLastError()}")
                return False
        else:
            # print(f"Failed to write memory at {hex(address)}. Error: {win32api.GetLastError()}")
            return False
    except Exception as e:
        print(f"Exception during write_memory at {hex(address)}: {e}")
        return False

def get_module_base_address(process_handle, module_name):
    """מחזיר את כתובת הבסיס של מודול בתהליך."""
    if not process_handle or not module_name: return None
    try:
        # הגדלת גודל המערך הראשוני למקרה שיש הרבה מודולים
        modules = win32process.EnumProcessModules(process_handle)
        for module_handle in modules:
            try:
                current_module_name = win32process.GetModuleFileNameEx(process_handle, module_handle)
                if module_name.lower() == os.path.basename(current_module_name).lower():
                    return module_handle # This is the base address (handle)
            except Exception:
                # יכולה להיות שגיאה בקבלת שם מודול מסוים (למשל 64 ביט מנסה לקרוא מודול 32 ביט ולהיפך במקרים מסוימים)
                continue # דלג למודול הבא
    except Exception as e:
        # שגיאה בקריאת EnumProcessModules עצמה (למשל, גישה נדחתה אם התהליך נסגר)
        print(f"Error enumerating modules: {e} (Error code: {win32api.GetLastError()})")
    return None

# --- פונקציות VM ו-Decryption (ללא שינוי) ---
def decrypt_string(encrypted_string):
    try:
        return base64.b64decode(encrypted_string).decode('utf-8')
    except Exception:
        return "Decryption Failed"

def is_running_in_vm():
    vm_indicators = ["VBOX", "VMWARE", "VIRTUAL", "HYPER-V"] # Add more if needed
    try:
        # Check Manufacturer and Model for VM indicators
        output = os.popen('wmic baseboard get product,Manufacturer').read().upper()
        for indicator in vm_indicators:
            if indicator in output:
                return True
        # Check ComputerSystem for VM indicators
        output_cs = os.popen('wmic computersystem get Model,Manufacturer').read().upper()
        for indicator in vm_indicators:
            if indicator in output_cs:
                return True
    except Exception:
        # Fallback or assume not VM if WMI fails
        pass
    return False

def hide_console_window():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 0) # SW_HIDE

# קלאס רקע (פשוט יותר, ללא טשטוש חיצוני)
class StaticBackground(tk.Canvas):
    def __init__(self, parent, bg_color='#101010'):
        super().__init__(parent, bg=bg_color, highlightthickness=0)
        # רקע סטטי, אין צורך ב-bind ל-Configure

# קלאס ראשי של תפריט המודים
class EnhancedModMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ZSCY Mod Menu v2")
        self.root.geometry("750x650") # גודל חלון

        self.selected_process = None
        self.process_handle = None
        self.module_base = None # לאחסון כתובת הבסיס
        self.feature_states = {feature: False for feature in BASE_OFFSETS.keys()}
        self.feature_buttons = {}
        self.dll_path = tk.StringVar(value=r"C:\path\to\your\default\cheat.dll") # נתיב ברירת מחדל ל-DLL
        self.gui_queue = queue.Queue() # תור לעדכוני GUI מ-threads

        # --- רקע סטטי ---
        self.background = StaticBackground(self.root, bg_color='#1a1a1a')
        self.background.pack(fill='both', expand=True)

        self.main_frame = tk.Frame(self.background, bg='#2a2a2a', bd=1, relief=tk.SOLID)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center', width=650, height=580)

        title_label = tk.Label(self.main_frame, text="ZSCY", font=("Arial", 36, "bold"), fg="#00ff00", bg='#2a2a2a')
        title_label.pack(pady=15)

        # --- אזור בחירת תהליך ---
        self.process_frame = tk.Frame(self.main_frame, bg='#2a2a2a')
        self.process_frame.pack(fill='x', pady=10, padx=20)

        self.process_btn = self.create_button("בחר תהליך משחק", self.select_process, parent=self.process_frame, width=20)
        self.process_btn.pack(side='left', padx=10)

        self.process_label = tk.Label(self.process_frame, text="לא נבחר תהליך", fg="#ff0000", bg='#2a2a2a', font=("Arial", 10))
        self.process_label.pack(side='left', padx=10, fill='x', expand=True)

        # --- יצירת טאבים ---
        self.create_category_tabs()

        # --- אזור הזרקת DLL ---
        self.dll_frame = tk.Frame(self.main_frame, bg='#2a2a2a')
        self.dll_frame.pack(fill='x', pady=10, padx=20, side=tk.BOTTOM) # Place at bottom

        dll_label = tk.Label(self.dll_frame, text="נתיב DLL:", fg="white", bg='#2a2a2a')
        dll_label.pack(side=tk.LEFT, padx=5)

        dll_entry = tk.Entry(self.dll_frame, textvariable=self.dll_path, width=40, bg='#333333', fg='white', insertbackground='white')
        dll_entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)

        browse_btn = self.create_button("עיון...", self.browse_dll, parent=self.dll_frame, width=8)
        browse_btn.pack(side=tk.LEFT, padx=5)

        inject_btn = self.create_button("הזרק DLL", self.inject_dll_threaded, parent=self.dll_frame, width=12)
        inject_btn.pack(side=tk.LEFT, padx=5)


        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.process_gui_queue() # התחל לבדוק את התור

    def process_gui_queue(self):
        """מעבד הודעות מהתור לעדכון ה-GUI."""
        try:
            while True:
                msg = self.gui_queue.get_nowait()
                if msg[0] == "messagebox":
                    messagebox.showinfo(msg[1], msg[2])
                elif msg[0] == "errorbox":
                     messagebox.showerror(msg[1], msg[2])
                # Add other message types if needed (e.g., update label)
        except queue.Empty:
            pass # No messages in queue
        self.root.after(100, self.process_gui_queue) # Check again after 100ms


    def create_button(self, text, command, parent=None, width=18):
        if parent is None:
            parent = self.main_frame
        btn = tk.Button(
            parent, text=text, command=command, font=("Arial", 10),
            bg='#333333', fg='white', activebackground='#00cc00',
            activeforeground='black', relief=tk.FLAT, width=width, pady=4
        )
        # Keep track of the original bg color for hover effect
        btn.original_bg = '#333333'
        btn.hover_bg = '#444444'
        btn.active_color = '#00ff00' # Green when feature is ON
        btn.bind("<Enter>", lambda e, b=btn: b.config(bg=b.hover_bg if not self.is_feature_active(b) else b.active_color))
        btn.bind("<Leave>", lambda e, b=btn: b.config(bg=b.original_bg if not self.is_feature_active(b) else b.active_color))
        # btn.pack(pady=4, padx=10, fill='x') # Packing is handled differently now (in tabs/grid)
        return btn

    def is_feature_active(self, btn):
       for feature_id, button in self.feature_buttons.items():
           if button == btn:
               return self.feature_states.get(feature_id, False)
       return False

    def update_button_state(self, feature_id, is_active):
        """Updates the visual state of a feature button."""
        button = self.feature_buttons.get(feature_id)
        if button:
            if is_active:
                button.config(bg=button.active_color, fg='black', activebackground='#00dd00') # Darker text on green
                 # Update hover color if mouse is currently over it
                if button.winfo_containing(button.winfo_pointerx(), button.winfo_pointery()) == button:
                     button.config(bg='#00cc00') # Slightly darker green on hover when active
            else:
                button.config(bg=button.original_bg, fg='white', activebackground='#00cc00')
                 # Update hover color if mouse is currently over it
                if button.winfo_containing(button.winfo_pointerx(), button.winfo_pointery()) == button:
                     button.config(bg=button.hover_bg)


    def create_category_tabs(self):
        self.notebook = ttk.Notebook(self.main_frame)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TNotebook", background='#2a2a2a', borderwidth=0)
        style.configure("TNotebook.Tab", background='#333333', foreground='white', padding=[10, 5], font=('Arial', 10))
        style.map("TNotebook.Tab", background=[("selected", "#00ff00")], foreground=[("selected", "black")])
        self.notebook.pack(fill='both', expand=True, padx=20, pady=10)

        for category_name, features in FEATURE_CATEGORIES.items():
            tab = tk.Frame(self.notebook, bg='#2a2a2a')
            self.notebook.add(tab, text=category_name)

            # Use grid layout within the tab for better alignment
            col_count = 0
            max_cols = 3 # Adjust number of columns as needed

            for feature_id, feature_name in features.items():
                if feature_id in BASE_OFFSETS:
                    # Create button but don't pack yet
                    btn = self.create_button(
                        feature_name,
                        lambda f=feature_id: self.toggle_feature(f),
                        tab,
                        width=20 # Slightly wider buttons
                    )
                    # Place button in grid
                    btn.grid(row=col_count // max_cols, column=col_count % max_cols, padx=5, pady=5, sticky='ew')
                    tab.grid_columnconfigure(col_count % max_cols, weight=1) # Make columns expand equally
                    self.feature_buttons[feature_id] = btn
                    col_count += 1


            if category_name == "כלי נשק":
                # Add separator and weapon buttons using grid
                sep = ttk.Separator(tab, orient='horizontal')
                sep.grid(row=(col_count + max_cols -1) // max_cols, column=0, columnspan=max_cols, sticky='ew', pady=10, padx=5)
                current_row = (col_count + max_cols -1) // max_cols + 1 # Start row after separator

                weapon_label = tk.Label(tab, text="הוספת נשקים בודדים:", font=("Arial", 12, "bold"), fg="#00ff00", bg='#2a2a2a')
                weapon_label.grid(row=current_row, column=0, columnspan=max_cols, pady=5)
                current_row += 1

                weapon_col = 0
                for weapon_name, weapon_id in WEAPONS.items():
                     btn = self.create_button(
                         f"החלף ל-{weapon_name}", # Changed text to reflect action
                         lambda w_id=weapon_id, w_name=weapon_name: self.set_current_weapon(w_id, w_name),
                         tab, width=15)
                     btn.grid(row=current_row + weapon_col // max_cols, column=weapon_col % max_cols, padx=5, pady=5, sticky='ew')
                     weapon_col += 1


    def get_feature_address(self, feature):
        """Calculates the dynamic address for a feature based on module base and offset."""
        if not self.module_base:
            messagebox.showerror("שגיאה", "כתובת הבסיס של המשחק לא נמצאה. האם התהליך הנכון נבחר והמודול קיים?")
            return None
        offset = BASE_OFFSETS.get(feature)
        if offset is None:
            messagebox.showerror("שגיאה", f"Offset עבור '{feature}' לא מוגדר.")
            return None
        return self.module_base + offset

    def toggle_feature(self, feature):
        if not self.process_handle:
            messagebox.showerror("שגיאה", "אנא בחר תהליך משחק תחילה!")
            return

        address = self.get_feature_address(feature)
        if address is None:
            return # Error message already shown by get_feature_address

        current_state = self.feature_states.get(feature, False)
        new_state = not current_state

        # --- לוגיקה לדוגמה לכתיבה ---
        # !!! יש להתאים את הערכים, סוגי הנתונים והגדלים לכל פיצ'ר במשחק הספציפי !!!
        success = False
        data_type = int # הנחה כללית
        data_size = 4   # הנחה כללית (DWORD)
        value_to_write = 1 if new_state else 0 # הנחה ל-Toggle (1=ON, 0=OFF)

        try:
            # התאמה ספציפית לפי סוג הפיצ'ר (דוגמאות)
            if feature in ["health", "armor", "money", "score", "speed", "jump"]:
                 # פיצ'רים של ערך - דורשים קלט מהמשתמש או ערך קבוע
                 # כרגע לא עושה כלום - נשאיר את זה כ-toggle לדוגמה, למרות ששם הפיצ'ר מצביע אחרת
                 # כדי לשנות ערך, תצטרך לקרוא את הערך הנוכחי או להוסיף Entry לקבלת קלט
                 # value_to_write = 9999 # או ערך שהוזן
                 # success = write_memory(self.process_handle, address, value_to_write, data_type, data_size)
                 print(f"Note: Feature '{feature}' might require specific value writing, not just toggle.")
                 success = write_memory(self.process_handle, address, value_to_write, data_type, data_size) # עדיין כותב 1/0 לדוגמה
            elif feature in ["ammo", "god_mode_flag", "no_clip_flag", "invisibility_flag"]:
                 # פיצ'רים של Toggle (דגל או פאץ')
                 success = write_memory(self.process_handle, address, value_to_write, data_type, data_size)
            elif feature == "current_weapon_id":
                 # דוגמה מורכבת יותר - קריאה ואז כתיבה
                 current_id = read_memory(self.process_handle, address, int, 4)
                 if current_id is not None:
                     next_id = (current_id % len(WEAPONS)) + 1 # עבור לנשק הבא ברשימה (דוגמה פשוטה)
                     success = write_memory(self.process_handle, address, next_id, int, 4)
                 else:
                    print(f"Could not read current weapon ID at {hex(address)}")
                    success = False
            else:
                print(f"No specific write logic defined for feature: {feature}")
                success = False # אין לוגיקה מוגדרת

            # --- עדכון מצב ותצוגה ---
            if success:
                self.feature_states[feature] = new_state
                self.update_button_state(feature, new_state) # עדכון צבע הכפתור
                status_text = "מופעל" if new_state else "מבוטל"
                # נסה למצוא שם ידידותי
                friendly_name = feature.replace('_', ' ').title()
                for cat, feats in FEATURE_CATEGORIES.items():
                    if feature in feats:
                        friendly_name = feats[feature]
                        break
                messagebox.showinfo("הצלחה", f"'{friendly_name}' {status_text}!")
            else:
                # אל תשנה את המצב הפנימי אם הכתיבה נכשלה
                messagebox.showerror("שגיאה בכתיבה לזיכרון", f"נכשל בשינוי מצב של '{feature}' בכתובת {hex(address)}.\nשגיאת כתיבה או שהערך/סוג אינו נכון. (Error code: {win32api.GetLastError()})")

        except Exception as e:
            print(f"Error toggling feature '{feature}': {e}")
            import traceback
            traceback.print_exc()
            messagebox.showerror("שגיאה קריטית", f"שגיאה לא צפויה בעת שינוי '{feature}': {str(e)}")

    # פונקציה להחלפת נשק (דוגמה)
    def set_current_weapon(self, weapon_id, weapon_name):
        feature = "current_weapon_id" # המזהה מה-Offsets
        if not self.process_handle:
            messagebox.showerror("שגיאה", "אנא בחר תהליך משחק תחילה!")
            return

        address = self.get_feature_address(feature)
        if address is None: return

        try:
            # נניח שה-ID נכתב כ-integer של 4 בתים
            if write_memory(self.process_handle, address, weapon_id, int, 4):
                 messagebox.showinfo("הצלחה", f"ניסיון להחליף נשק ל-{weapon_name} (ID: {weapon_id}) הצליח (כתיבה בוצעה).")
                 # כאן אפשר לעדכן גם את ה-state של הפיצ'ר הראשי אם רוצים
                 # self.feature_states[feature] = True # או משהו דומה
            else:
                 messagebox.showerror("שגיאה בכתיבה", f"נכשל בכתיבת ID הנשק {weapon_id} לכתובת {hex(address)}. (Error code: {win32api.GetLastError()})")
        except Exception as e:
            print(f"Error setting weapon ID {weapon_id}: {e}")
            messagebox.showerror("שגיאה קריטית", f"שגיאה לא צפויה בהחלפת נשק: {str(e)}")

    def select_process(self):
        # --- ניקוי מצב קודם ---
        if self.process_handle:
            try: win32api.CloseHandle(self.process_handle)
            except: pass
            self.process_handle = None
            self.selected_process = None
            self.module_base = None
            self.process_label.config(text="לא נבחר תהליך", fg="#ff0000")
            # Reset feature states and button colors
            for feature_id in self.feature_states:
                self.feature_states[feature_id] = False
                self.update_button_state(feature_id, False)


        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name']):
                try: processes.append((proc.info['name'], proc.info['pid']))
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess): pass

            process_window = tk.Toplevel(self.root)
            # ... (שאר קוד חלון בחירת תהליך - כמעט ללא שינוי) ...
            process_window.title("בחר תהליך משחק")
            process_window.geometry("450x550")
            process_window.configure(bg='#1a1a1a')
            process_window.attributes('-topmost', True)

            search_frame = tk.Frame(process_window, bg='#1a1a1a')
            search_frame.pack(fill='x', padx=10, pady=10)
            search_label = tk.Label(search_frame, text="חיפוש:", font=("Arial", 10), fg="white", bg='#1a1a1a')
            search_label.pack(side='left', padx=5)
            search_var = tk.StringVar()
            search_entry = tk.Entry(search_frame, textvariable=search_var, font=("Arial", 10), bg='#333333', fg='white', insertbackground='white')
            search_entry.pack(side='left', fill='x', expand=True, padx=5)
            search_entry.focus()

            frame = tk.Frame(process_window, bg='#1a1a1a')
            frame.pack(fill='both', expand=True, padx=10, pady=5)
            scrollbar = tk.Scrollbar(frame)
            scrollbar.pack(side='right', fill='y')
            listbox = tk.Listbox(
                frame, bg='#333333', fg='white', selectmode='single',
                yscrollcommand=scrollbar.set, font=("Arial", 10),
                selectbackground="#00ff00", selectforeground="black"
            )
            listbox.pack(side='left', fill='both', expand=True)
            scrollbar.config(command=listbox.yview)

            processes.sort(key=lambda x: x[0].lower())
            all_processes = processes.copy() # חשוב לשמור עותק לא מסונן

            for proc_name, proc_pid in processes:
                listbox.insert('end', f"{proc_name} (PID: {proc_pid})")

            def filter_processes(*args):
                search_term = search_var.get().lower()
                listbox.delete(0, tk.END)
                for proc_name, proc_pid in all_processes: # לסנן מהעותק המלא
                    if search_term in proc_name.lower():
                        listbox.insert('end', f"{proc_name} (PID: {proc_pid})")

            search_var.trace('w', filter_processes)

            def on_select(event=None):
                if not listbox.curselection(): return
                selected_index = listbox.curselection()[0]
                selected_text = listbox.get(selected_index)

                try:
                    pid_str = selected_text.split('PID: ')[1].replace(')', '')
                    proc_pid = int(pid_str)
                    proc_name = selected_text.split(' (PID:')[0]

                    # --- ניסיון פתיחת תהליך וקבלת כתובת בסיס ---
                    try:
                        # בקש רק את ההרשאות שאנחנו באמת צריכים
                        self.process_handle = win32api.OpenProcess(REQUIRED_ACCESS, False, proc_pid)
                        self.selected_process = proc_pid

                        # נסה למצוא את כתובת הבסיס של המודול
                        self.module_base = get_module_base_address(self.process_handle, GAME_MODULE_NAME)

                        if self.module_base:
                            self.process_label.config(text=f"נבחר: {proc_name} (PID: {proc_pid}) | בסיס: {hex(self.module_base)}", fg="#00ff00")
                            messagebox.showinfo("הצלחה", f"התהליך '{proc_name}' נבחר וכתובת הבסיס ({hex(self.module_base)}) נמצאה.")
                        else:
                            # אם כתובת הבסיס לא נמצאה, עדיין אפשר להמשיך, אבל להזהיר
                            self.process_label.config(text=f"נבחר: {proc_name} (PID: {proc_pid}) | בסיס לא נמצא!", fg="#ffff00") # צהוב אזהרה
                            messagebox.showwarning("אזהרה", f"התהליך '{proc_name}' נבחר, אך לא נמצא המודול '{GAME_MODULE_NAME}'.\nודא שהשם נכון ושהמשחק רץ. הפיצ'רים לא יעבדו ללא כתובת בסיס.")
                            # במקרה כזה, לא לסגור את החלון כדי לאפשר בחירה חוזרת
                            # process_window.destroy() # << לא לסגור כאן
                            return # חזור לחלון הבחירה

                        process_window.destroy() # סגור רק אם הכל תקין

                    except Exception as open_error:
                        last_error = win32api.GetLastError()
                        error_msg = f"לא ניתן לפתוח את התהליך {proc_name} (PID: {proc_pid}).\n"
                        if last_error == 5: # Access Denied
                           error_msg += "שגיאת גישה (Error 5). ודא שהתוכנה רצה כמנהל (Administrator).\n"
                        else:
                           error_msg += f"שגיאה: {open_error} (קוד: {last_error})\n"
                        print(f"Error opening process {proc_pid}: {open_error} (Code: {last_error})")
                        messagebox.showerror("שגיאה בפתיחת תהליך", error_msg)
                        if self.process_handle: # נקה אם נפתח חלקית
                            try: win32api.CloseHandle(self.process_handle)
                            except: pass
                        self.process_handle = None
                        self.selected_process = None
                        self.module_base = None
                        self.process_label.config(text="בחירת תהליך נכשלה", fg="#ff0000")

                except (IndexError, ValueError) as parse_error:
                    print(f"Error parsing selected process string '{selected_text}': {parse_error}")
                    messagebox.showerror("שגיאה", "שגיאה בעיבוד בחירת התהליך.")

            listbox.bind("<Double-Button-1>", on_select)
            button_frame = tk.Frame(process_window, bg='#1a1a1a')
            button_frame.pack(fill='x', padx=10, pady=10)
            select_btn = tk.Button(button_frame, text="בחר", command=on_select, font=("Arial", 10), bg='#333333', fg='white', activebackground='#00ff00', activeforeground='black', relief=tk.FLAT, width=10)
            select_btn.pack(side='right', padx=5)
            cancel_btn = tk.Button(button_frame, text="בטל", command=process_window.destroy, font=("Arial", 10), bg='#333333', fg='white', activebackground='#ff0000', activeforeground='black', relief=tk.FLAT, width=10)
            cancel_btn.pack(side='right', padx=5)

        except Exception as e:
             print(f"Error getting process list: {e}")
             import traceback
             traceback.print_exc()
             messagebox.showerror("שגיאה", f"נכשל בקבלת רשימת התהליכים: {str(e)}")

    def browse_dll(self):
        """Opens a file dialog to select a DLL."""
        filepath = filedialog.askopenfilename(
            title="בחר קובץ DLL",
            filetypes=(("Dynamic Link Library", "*.dll"), ("All files", "*.*"))
        )
        if filepath:
            self.dll_path.set(filepath)

    def inject_dll_threaded(self):
        """Starts the DLL injection in a separate thread."""
        if not self.process_handle:
             messagebox.showerror("שגיאה", "אנא בחר תהליך משחק תחילה!")
             return

        dll_to_inject = self.dll_path.get()
        if not dll_to_inject or not os.path.exists(dll_to_inject):
             messagebox.showerror("שגיאה", f"קובץ DLL לא נמצא או לא נבחר:\n{dll_to_inject}")
             return

        # הפעל את ההזרקה ב-thread נפרד
        injection_thread = threading.Thread(target=self.inject_dll_logic, args=(self.process_handle, dll_to_inject), daemon=True)
        injection_thread.start()
        messagebox.showinfo("הזרקה", "תהליך הזרקת DLL החל ברקע...")


    def inject_dll_logic(self, process_handle_local, dll_path):
        """The actual DLL injection logic (runs in a separate thread)."""
        # חשוב: הפונקציה רצה ב thread נפרד. עדכוני GUI צריכים לעבור דרך התור.
        remote_memory = None
        thread_handle = None
        kernel32 = None
        load_library_addr = None

        try:
            if not process_handle_local:
                 raise Exception("Process handle is invalid for injection.")

            if not os.path.exists(dll_path):
                raise FileNotFoundError(f"DLL file not found at: {dll_path}")

            path_bytes = (dll_path + '\0').encode('utf-8')
            path_size = len(path_bytes)

            # הקצאת זיכרון
            remote_memory = win32process.VirtualAllocEx(
                process_handle_local, 0, path_size,
                win32con.MEM_COMMIT | win32con.MEM_RESERVE, win32con.PAGE_READWRITE
            )
            if not remote_memory:
                raise Exception(f"Failed to allocate memory. Error: {win32api.GetLastError()}")

            # כתיבת נתיב ה-DLL
            bytes_written = ctypes.c_size_t() # Explicitly create c_size_t for byref
            if not win32process.WriteProcessMemory(process_handle_local, remote_memory, path_bytes, path_size, ctypes.byref(bytes_written)) or bytes_written.value != path_size:
                 raise Exception(f"Failed to write DLL path. Wrote {bytes_written.value}/{path_size}. Error: {win32api.GetLastError()}")


            # קבלת כתובת LoadLibraryA
            kernel32 = win32api.GetModuleHandle('kernel32.dll')
            load_library_addr = win32api.GetProcAddress(kernel32, 'LoadLibraryA')
            if not load_library_addr:
                raise Exception(f"Failed to get LoadLibraryA address. Error: {win32api.GetLastError()}")

            # יצירת תהליכון מרוחק
            thread_handle, thread_id = win32process.CreateRemoteThread(
                process_handle_local, None, 0, load_library_addr, remote_memory, 0, None
            )
            if not thread_handle:
                raise Exception(f"Failed to create remote thread. Error: {win32api.GetLastError()}")

            # המתנה לסיום התהליכון
            wait_result = win32event.WaitForSingleObject(thread_handle, 15000) # Timeout 15 שניות

            if wait_result == win32event.WAIT_TIMEOUT:
                 print("Warning: Remote thread (LoadLibrary) timed out.")
                 # אפשר לנסות להרוג את ה-thread אם נתקע, אבל זה מסוכן
                 # win32process.TerminateThread(thread_handle, -1)
                 raise Exception("Remote thread timed out.")
            elif wait_result != win32event.WAIT_OBJECT_0:
                 raise Exception(f"WaitForSingleObject failed. Result: {wait_result}, Error: {win32api.GetLastError()}")


            # בדוק את קוד היציאה של LoadLibrary (אם אפשר ורלוונטי)
            # exit_code = win32process.GetExitCodeThread(thread_handle)
            # if exit_code == 0: # LoadLibrary מחזירה 0 בכישלון (לרוב)
            #    print("Warning: LoadLibrary might have failed in the remote process (returned 0).")


            # שלח הודעת הצלחה לתור ה-GUI
            self.gui_queue.put(("messagebox", "הצלחה", "DLL הוזרק בהצלחה!"))

        except FileNotFoundError as fnf_error:
             self.gui_queue.put(("errorbox", "שגיאה בהזרקת DLL", str(fnf_error)))
        except Exception as e:
            last_error = win32api.GetLastError()
            error_details = f"נכשל בהזרקת DLL: {str(e)}\n(Error Code: {last_error})"
            print(f"Error injecting DLL: {e} (Code: {last_error})")
            import traceback
            traceback.print_exc()
            self.gui_queue.put(("errorbox", "שגיאה בהזרקת DLL", error_details))
        finally:
            # --- ניקוי ---
            if thread_handle:
                try: win32api.CloseHandle(thread_handle)
                except: pass
            if remote_memory and process_handle_local: # בדוק ששניהם קיימים
                try: win32process.VirtualFreeEx(process_handle_local, remote_memory, 0, win32con.MEM_RELEASE)
                except: pass
            # אין לסגור את process_handle_local כאן כי הוא הראשי מהמחלקה

    def on_closing(self):
        print("Closing application and releasing process handle...")
        if self.process_handle:
            try:
                win32api.CloseHandle(self.process_handle)
                self.process_handle = None
                self.selected_process = None
                self.module_base = None
            except Exception as e:
                print(f"Error closing process handle: {e}")
        self.root.destroy()

    def run(self):
        self.root.mainloop()

# נקודת הכניסה הראשית
if __name__ == "__main__":
    # בדיקת הרשאות מנהל
    is_admin = False
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        print("Could not determine admin status using ctypes.")
        is_admin = False # Assume not admin if check fails

    if not is_admin:
        messagebox.showerror("שגיאה", "תוכנה זו דורשת הרשאות מנהל (Administrator) כדי לגשת לזיכרון של תהליכים אחרים.\nאנא הפעל מחדש כמנהל.")
        sys.exit(1)

    # בדיקת סביבה וירטואלית (בסיסית)
    if is_running_in_vm():
        if messagebox.askyesno("אזהרה", "זוהתה ריצה בסביבה וירטואלית (VM).\nהאם ברצונך להמשיך בכל זאת? (לא מומלץ)"):
            print("Warning: Running in a Virtual Machine.")
        else:
            print("Exiting due to VM detection.")
            sys.exit(1)

    # הסתרת חלון הקונסולה (אם רלוונטי)
    hide_console_window()

    # הדגמת פענוח (ללא שינוי)
    encrypted_payload = "U29tZSBlbmNyeXB0ZWQgcGF5bG9hZA=="
    decrypted_payload = decrypt_string(encrypted_payload)
    print(f"Decrypted payload example: {decrypted_payload}") # יודפס לקונסול הנסתר או ל-IDE

    # יצירת מופע והפעלה
    menu = EnhancedModMenu()
    menu.run()