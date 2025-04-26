# -*- coding: utf-8 -*-

# Code generated/updated: Thursday, April 17, 2025 

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
from PIL import Image, ImageTk # Keep if using static images or icons
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
ERROR_ACCESS_DENIED = 5

REQUIRED_ACCESS = (
    PROCESS_QUERY_INFORMATION | PROCESS_VM_OPERATION |
    PROCESS_VM_READ | PROCESS_VM_WRITE | PROCESS_CREATE_THREAD
)

# !!! שנה לשם המודול הראשי של המשחק (לרוב שם קובץ ה-EXE) !!!
GAME_MODULE_NAME = "ac_client.exe" # דוגמה: Assault Cube

# =============================================================================
# !!! אזהרה חמורה: ה-Offsets הבאים הם Placeholders בלבד (0x0)! !!!
# !!! עליך להחליף אותם ב-Offsets האמיתיים מהמשחק הספציפי שלך,  !!!
# !!! שנמצאו באמצעות כלים כמו Cheat Engine, יחסית לכתובת     !!!
# !!! הבסיס של המודול שהוגדר ב-GAME_MODULE_NAME.             !!!
# !!! ללא Offsets נכונים, התוכנה לא תעבוד ותכתוב לכתובות שגויות! !!!
# =============================================================================
BASE_OFFSETS = {
    "health": 0x00109B74, "armor": 0x00109B78, "ammo": 0x00109B80,
    "money": 0x00109F78, "level": 0x0010A000, "weapons_struct_ptr": 0x00109B84,
    "current_weapon_id": 0x00109B88, "speed": 0x00109C00, "jump": 0x00109C04,
    "god_mode_flag": 0x0010A123, "no_clip_flag": 0x0010A456,
    "invisibility_flag": 0x0010A789
} # דוגמאות AC - החלף באופסטים שלך!

# ============= רשימת כלי נשק (התאם למשחק) =============
WEAPONS = { "Pistol": 1, "Shotgun": 2, "SMG": 3, "Rifle": 4, "Sniper": 5, "RPG": 6, "Grenade": 7, "Knife": 8 }

# ============= קטגוריות פיצ'רים (עדכון שמות והפרדה לוגית) =============
VALUE_FEATURES = {"health", "armor", "money", "level", "speed"}
TOGGLE_FEATURES = {"ammo", "god_mode_flag", "no_clip_flag", "invisibility_flag"}
SPECIAL_FEATURES = {"weapons_struct_ptr", "current_weapon_id", "jump"}

FEATURE_CATEGORIES = {
    "נתוני שחקן": {
        "health": "חיים (קבע ערך)", "armor": "שריון (קבע ערך)",
        "ammo": "תחמושת אינסופית (Toggle)", "money": "כסף (קבע ערך)",
        "level": "רמה (קבע ערך)"
    },
    "כלי נשק": { "current_weapon_id": "החלף לנשק הבא (דוגמה)" },
    "תנועה": { "speed": "מהירות (קבע ערך)", "no_clip_flag": "מעבר דרך קירות (Toggle)" },
    "שונות": { "god_mode_flag": "מצב אלוהים (Toggle)", "invisibility_flag": "אי-נראות (Toggle)" }
}

# --- פונקציות עזר לזיכרון, VM, Decryption (ללא שינוי מהותי) ---
def read_memory(process_handle, address, data_type, size):
    """קורא זיכרון מכתובת ספציפית."""
    if not process_handle or not address: return None
    buffer = ctypes.create_string_buffer(size)
    bytes_read = ctypes.c_size_t()
    try:
        if win32process.ReadProcessMemory(process_handle, address, buffer, size, ctypes.byref(bytes_read)):
            if bytes_read.value == size:
                # --- המרות סוגים ---
                if data_type == int:
                    if size == 4: return ctypes.cast(buffer, ctypes.POINTER(wintypes.DWORD))[0]
                    if size == 8: return ctypes.cast(buffer, ctypes.POINTER(ctypes.c_ulonglong))[0]
                    if size == 2: return ctypes.cast(buffer, ctypes.POINTER(wintypes.WORD))[0]
                    if size == 1: return ctypes.cast(buffer, ctypes.POINTER(wintypes.BYTE))[0]
                elif data_type == float:
                    if size == 4: return ctypes.cast(buffer, ctypes.POINTER(ctypes.c_float))[0]
                    if size == 8: return ctypes.cast(buffer, ctypes.POINTER(ctypes.c_double))[0]
                elif data_type == bytes: return buffer.raw[:bytes_read.value]
                # --- ---
                print(f"Read Warning: Unsupported type/size: {data_type}/{size}")
                return buffer.raw[:bytes_read.value] # fallback
            # else: print(f"Read Error: Read {bytes_read.value}/{size} bytes.")
        # else: print(f"Failed ReadProcessMemory. Error: {win32api.GetLastError()}")
    except Exception as e: print(f"Exception during read_memory: {e}")
    return None

def write_memory(process_handle, address, value, data_type, size):
    """כותב זיכרון לכתובת ספציפית."""
    if not process_handle or not address: return False
    c_value = None
    try:
        target_type = None
        if data_type == int:
            if size == 4: target_type = wintypes.DWORD
            elif size == 8: target_type = ctypes.c_ulonglong
            elif size == 2: target_type = wintypes.WORD
            elif size == 1: target_type = wintypes.BYTE
        elif data_type == float:
            if size == 4: target_type = ctypes.c_float
            elif size == 8: target_type = ctypes.c_double
        elif data_type == bytes:
             if isinstance(value, bytes): c_value = ctypes.create_string_buffer(value, size)
             else: return False
        else: return False

        if target_type: c_value = target_type(data_type(value)) # Convert to python type then ctype

        if c_value is None and data_type != bytes: return False

        bytes_written = ctypes.c_size_t()
        if win32process.WriteProcessMemory(process_handle, address, ctypes.byref(c_value), size, ctypes.byref(bytes_written)):
            return bytes_written.value == size
        # else: print(f"Failed WriteProcessMemory. Error: {win32api.GetLastError()}")
    except ValueError as ve: print(f"Write Error: Invalid value type for {data_type}: {value} - {ve}")
    except Exception as e: print(f"Exception during write_memory: {e}")
    return False

def get_module_base_address(process_handle, module_name):
    """מחזיר את כתובת הבסיס של מודול בתהליך."""
    if not process_handle or not module_name: return None
    try:
        modules = win32process.EnumProcessModules(process_handle)
        for module_handle in modules:
            try:
                current_module_name = win32process.GetModuleFileNameEx(process_handle, module_handle)
                if module_name.lower() == os.path.basename(current_module_name).lower():
                    return module_handle
            except Exception: continue # Ignore specific module errors
    except Exception as e: print(f"Error enumerating modules: {e}")
    return None

def decrypt_string(encrypted_string):
    try: return base64.b64decode(encrypted_string).decode('utf-8')
    except Exception: return "Decryption Failed"

def is_running_in_vm():
    vm_indicators = ["VBOX", "VMWARE", "VIRTUAL", "HYPER-V", "XEN"]
    try:
        # Check Baseboard and ComputerSystem WMI objects
        output_bb = os.popen('wmic baseboard get product,Manufacturer').read().upper()
        if any(indicator in output_bb for indicator in vm_indicators): return True
        output_cs = os.popen('wmic computersystem get Model,Manufacturer').read().upper()
        if any(indicator in output_cs for indicator in vm_indicators): return True
    except Exception: pass
    return False

def hide_console_window():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd: ctypes.windll.user32.ShowWindow(hwnd, 0)

# קלאס רקע סטטי
class StaticBackground(tk.Canvas):
    def __init__(self, parent, bg_color='#101010'):
        super().__init__(parent, bg=bg_color, highlightthickness=0)

# קלאס ראשי של תפריט המודים
class EnhancedModMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ZSCY Mod Menu v3.2 - Syntax Corrected")
        self.root.geometry("750x700")

        # --- משתני מחלקה ---
        self.selected_process = None
        self.process_handle = None
        self.module_base = None
        self.feature_states = {feature: False for feature in BASE_OFFSETS.keys()}
        self.feature_buttons = {}
        self.dll_path = tk.StringVar(value=r"C:\temp\mycheat.dll") # נתיב ברירת מחדל לדוגמה
        self.gui_queue = queue.Queue()
        self.value_frames = {}
        self.value_vars = {}
        self.value_entries = {}

        # --- הגדרות GUI ראשיות ---
        self.background = StaticBackground(self.root, bg_color='#1a1a1a')
        self.background.pack(fill='both', expand=True)
        self.main_frame = tk.Frame(self.background, bg='#2a2a2a', bd=1, relief=tk.SOLID)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center', width=650, height=630)
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
        self.dll_frame.pack(fill='x', pady=10, padx=20, side=tk.BOTTOM)
        dll_label = tk.Label(self.dll_frame, text="נתיב DLL:", fg="white", bg='#2a2a2a'); dll_label.pack(side=tk.LEFT, padx=5)
        dll_entry = tk.Entry(self.dll_frame, textvariable=self.dll_path, width=40, bg='#333333', fg='white', insertbackground='white'); dll_entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)
        browse_btn = self.create_button("עיון...", self.browse_dll, parent=self.dll_frame, width=8); browse_btn.pack(side=tk.LEFT, padx=5)
        inject_btn = self.create_button("הזרק DLL", self.inject_dll_threaded, parent=self.dll_frame, width=12); inject_btn.pack(side=tk.LEFT, padx=5)

        # --- הגדרות סיום ---
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.process_gui_queue() # התחל לבדוק את תור ההודעות ל-GUI

    def process_gui_queue(self):
        """מעבד הודעות מהתור לעדכון ה-GUI."""
        try:
            while True:
                msg_type, title, message = self.gui_queue.get_nowait() # שינוי לקבל 3 ערכים
                if msg_type == "messagebox": messagebox.showinfo(title, message)
                elif msg_type == "errorbox": messagebox.showerror(title, message)
        except queue.Empty: pass
        except Exception as e: print(f"Error processing GUI queue: {e}") # תפוס שגיאות אחרות
        self.root.after(100, self.process_gui_queue) # בדוק שוב

    def create_button(self, text, command, parent=None, width=18):
        """יוצר כפתור מעוצב."""
        # ... (קוד יצירת כפתור כמו קודם, ללא שינוי) ...
        if parent is None: parent = self.main_frame
        btn = tk.Button( parent, text=text, command=command, font=("Arial", 10),
            bg='#333333', fg='white', activebackground='#00cc00',
            activeforeground='black', relief=tk.FLAT, width=width, pady=4 )
        btn.original_bg = '#333333'; btn.hover_bg = '#444444'; btn.active_color = '#00ff00'
        btn.bind("<Enter>", lambda e, b=btn: b.config(bg=b.hover_bg if not self.is_feature_or_input_active(b) else b.active_color))
        btn.bind("<Leave>", lambda e, b=btn: b.config(bg=b.original_bg if not self.is_feature_or_input_active(b) else b.active_color))
        return btn

    def is_feature_or_input_active(self, btn):
       """בודק אם פיצ'ר/קלט משויך פעיל."""
       for feature_id, button in self.feature_buttons.items():
           if button == btn: return self.feature_states.get(feature_id, False)
       return False

    def update_button_state(self, feature_id, is_active):
        """מעדכן צבע כפתור בהתאם למצב."""
        # ... (קוד עדכון כפתור כמו קודם, ללא שינוי) ...
        button = self.feature_buttons.get(feature_id)
        if button:
            active_bg = button.active_color; inactive_bg = button.original_bg
            hover_active_bg = '#00cc00'; hover_inactive_bg = button.hover_bg
            current_bg = button.cget('bg') # קבל צבע נוכחי כדי לבדוק אם העכבר מעל
            is_hover = current_bg == hover_active_bg or current_bg == hover_inactive_bg

            if is_active:
                button.config(bg=hover_active_bg if is_hover else active_bg, fg='black', activebackground=hover_active_bg)
            else:
                button.config(bg=hover_inactive_bg if is_hover else inactive_bg, fg='white', activebackground=hover_active_bg)


    def create_category_tabs(self):
        """יוצר את הטאבים ואת התוכן שלהם."""
        self.notebook = ttk.Notebook(self.main_frame)
        # ... (הגדרות סגנון ttk כמו קודם) ...
        style = ttk.Style(); style.theme_use('clam')
        style.configure("TNotebook", background='#2a2a2a', borderwidth=0)
        style.configure("TNotebook.Tab", background='#333333', foreground='white', padding=[10, 5], font=('Arial', 10))
        style.map("TNotebook.Tab", background=[("selected", "#00ff00")], foreground=[("selected", "black")])
        self.notebook.pack(fill='both', expand=True, padx=20, pady=10)

        # --- רישום פונקציות ולידציה ---
        validate_int_cmd = (self.root.register(self.validate_integer_input), '%P')
        validate_float_cmd = (self.root.register(self.validate_float_input), '%P')

        for category_name, features in FEATURE_CATEGORIES.items():
            tab = tk.Frame(self.notebook, bg='#2a2a2a')
            self.notebook.add(tab, text=category_name)
            max_cols = 3
            feature_row_index = 0

            for feature_id, feature_name in features.items():
                if feature_id in BASE_OFFSETS:
                    is_value_feature = feature_id in VALUE_FEATURES
                    btn_command = self.toggle_value_input if is_value_feature else self.toggle_feature
                    # קביעת ולידציה
                    validation_cmd = None
                    if feature_id == "speed": validation_cmd = validate_float_cmd
                    elif is_value_feature: validation_cmd = validate_int_cmd

                    # --- יצירת כפתור ראשי ווידג'טים של קלט ---
                    btn = self.create_button(feature_name, lambda f=feature_id: btn_command(f), tab, width=20)
                    grid_col = (feature_row_index % max_cols)
                    grid_row = (feature_row_index // max_cols) * 2 # שורה זוגית לכפתור
                    btn.grid(row=grid_row, column=grid_col, padx=5, pady=(5, 0), sticky='ew')
                    tab.grid_columnconfigure(grid_col, weight=1)
                    self.feature_buttons[feature_id] = btn

                    if is_value_feature:
                        # --- מסגרת הקלט ---
                        value_frame = tk.Frame(tab, bg='#2a2a2a')
                        value_frame.grid(row=grid_row + 1, column=grid_col, padx=5, pady=(0, 10), sticky='ew') # שורה אי-זוגית
                        self.value_frames[feature_id] = value_frame
                        # --- ווידג'טים בתוך המסגרת ---
                        lbl = tk.Label(value_frame, text="ערך:", fg="white", bg='#2a2a2a', font=("Arial", 9)); lbl.pack(side=tk.LEFT, padx=(0, 5))
                        var = tk.StringVar(); self.value_vars[feature_id] = var
                        entry = tk.Entry(value_frame, textvariable=var, width=10, bg='#333333', fg='white',insertbackground='white', font=("Arial", 9), validate='key', validatecommand=validation_cmd); entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True); self.value_entries[feature_id] = entry
                        set_btn = tk.Button(value_frame, text="קבע", font=("Arial", 8, "bold"), command=lambda f=feature_id: self.set_feature_value(f), bg='#009900', fg='white', activebackground='#00cc00', relief=tk.FLAT, padx=5); set_btn.pack(side=tk.LEFT, padx=(5, 0))
                        value_frame.grid_remove() # הסתר בהתחלה

                    feature_row_index += 1

            # --- טיפול בטאב כלי נשק ---
            if category_name == "כלי נשק":
                # ... (קוד יצירת כפתורי נשק כמו קודם) ...
                weapon_start_row = (feature_row_index + max_cols -1) // max_cols * 2
                sep = ttk.Separator(tab, orient='horizontal'); sep.grid(row=weapon_start_row, column=0, columnspan=max_cols, sticky='ew', pady=10, padx=5); weapon_start_row += 1
                weapon_label = tk.Label(tab, text="החלפת נשק נוכחי:", font=("Arial", 12, "bold"), fg="#00ff00", bg='#2a2a2a'); weapon_label.grid(row=weapon_start_row, column=0, columnspan=max_cols, pady=5); weapon_start_row += 1
                weapon_col = 0
                for weapon_name, weapon_id in WEAPONS.items():
                     btn = self.create_button(f"{weapon_name}", lambda w_id=weapon_id, w_name=weapon_name: self.set_current_weapon(w_id, w_name), tab, width=15)
                     btn.grid(row=weapon_start_row + weapon_col // max_cols, column=weapon_col % max_cols, padx=5, pady=5, sticky='ew')
                     weapon_col += 1

    # ====> פונקציות ולידציה לקלט <====
    def validate_integer_input(self, P):
        """מאפשר רק ספרות או מחרוזת ריקה."""
        return P == "" or P.isdigit()

    def validate_float_input(self, P):
        """מאפשר מספרים שלמים או צפים (עם נקודה אחת)."""
        if P in ["", "-"]: return True
        if P.count('.') > 1: return False
        cleaned = P.replace('.', '', 1).replace('-', '', 1)
        return cleaned.isdigit()

    def get_feature_address(self, feature):
        """מחזיר את הכתובת הדינמית של הפיצ'ר."""
        if not self.module_base: messagebox.showerror("שגיאה", "כתובת בסיס לא נמצאה."); return None
        offset = BASE_OFFSETS.get(feature)
        if offset is None: messagebox.showerror("שגיאה", f"Offset '{feature}' לא מוגדר."); return None
        if offset == 0 and feature != "module_base": # Reminder for placeholder offsets
             messagebox.showwarning("אזהרה", f"Offset עבור '{feature}' הוא 0x0. ודא שהחלפת אותו!")
        return self.module_base + offset

    def toggle_value_input(self, feature_id):
        """מציג/מסתיר שדה קלט לפיצ'ר ערך."""
        # ... (קוד זהה לקודם) ...
        if feature_id not in self.value_frames: return
        frame = self.value_frames[feature_id]
        current_state = self.feature_states.get(feature_id, False)
        new_state = not current_state
        if new_state: frame.grid()
        else: frame.grid_remove()
        self.feature_states[feature_id] = new_state
        self.update_button_state(feature_id, new_state)

    def set_feature_value(self, feature_id):
        """קורא ערך מה-Entry וכותב לזיכרון."""
        # ... (קוד זהה לקודם, עם קביעת סוג/גודל) ...
        if not self.process_handle: messagebox.showerror("שגיאה", "בחר תהליך!"); return
        if feature_id not in self.value_vars: messagebox.showerror("שגיאה", f"שדה קלט '{feature_id}' לא קיים."); return
        address = self.get_feature_address(feature_id)
        if address is None: return
        value_str = self.value_vars[feature_id].get()
        if not value_str: messagebox.showerror("שגיאת קלט", "הזן ערך."); return

        # !!! קבע סוג וגודל נתונים נכון למשחק !!!
        data_type = int; data_size = 4
        if feature_id == "speed": data_type = float; data_size = 4
        # ... הוסף עוד התאמות ...

        try: value_to_write = data_type(value_str)
        except ValueError: messagebox.showerror("שגיאת קלט", f"ערך '{value_str}' שגוי עבור {data_type.__name__}."); return

        try:
            if write_memory(self.process_handle, address, value_to_write, data_type, data_size):
                messagebox.showinfo("הצלחה", f"ערך {value_to_write} נקבע עבור '{feature_id}'.")
            else: messagebox.showerror("שגיאה בכתיבה", f"נכשל בכתיבת {value_to_write} לכתובת {hex(address)}.\n(שגיאה: {win32api.GetLastError()})")
        except Exception as e: messagebox.showerror("שגיאה קריטית", f"שגיאה בקביעת ערך '{feature_id}': {str(e)}")


    def toggle_feature(self, feature):
        """מטפל בפיצ'רים שהם Toggle."""
        # ... (קוד זהה לקודם, עם קביעת סוג/גודל) ...
        if feature not in TOGGLE_FEATURES:
             if feature in VALUE_FEATURES: self.toggle_value_input(feature); return
             print(f"'{feature}' is not a toggle feature."); return

        if not self.process_handle: messagebox.showerror("שגיאה", "בחר תהליך!"); return
        address = self.get_feature_address(feature)
        if address is None: return
        current_state = self.feature_states.get(feature, False)
        new_state = not current_state

        # !!! קבע סוג, גודל, וערך נכון למשחק !!!
        data_type = int; data_size = 4
        value_to_write = 1 if new_state else 0

        print(f"Attempting to toggle '{feature}' at {hex(address)} to state {value_to_write}")
        try:
            if write_memory(self.process_handle, address, value_to_write, data_type, data_size):
                self.feature_states[feature] = new_state
                self.update_button_state(feature, new_state)
                status_text = "מופעל" if new_state else "מבוטל"
                friendly_name = feature.replace('_', ' ').title()
                for cat, feats in FEATURE_CATEGORIES.items():
                    if feature in feats: friendly_name = feats[feature]; break
                messagebox.showinfo("הצלחה", f"'{friendly_name}' {status_text}!")
            else: messagebox.showerror("שגיאה בכתיבה", f"נכשל בשינוי Toggle '{feature}'.\n(שגיאה: {win32api.GetLastError()})")
        except Exception as e: messagebox.showerror("שגיאה קריטית", f"שגיאה ב-Toggle '{feature}': {str(e)}")

    def select_process(self):
        """פותח חלון לבחירת תהליך, פותח Handle ומוצא כתובת בסיס."""
        # --- ניקוי מצב קודם ---
        if self.process_handle:
            try: win32api.CloseHandle(self.process_handle); self.process_handle = None
            except Exception as e: print(f"Note: Error closing previous handle: {e}")
        self.selected_process = None; self.module_base = None
        self.process_label.config(text="לא נבחר תהליך", fg="#ff0000")
        for feature_id in BASE_OFFSETS.keys(): # איפוס כל המצבים והתצוגה
            self.feature_states[feature_id] = False
            self.update_button_state(feature_id, False)
            if feature_id in self.value_frames:
                self.value_frames[feature_id].grid_remove()
                if feature_id in self.value_vars: self.value_vars[feature_id].set("")

        # --- חלון בחירה ---
        try:
            processes = [(p.info['name'], p.info['pid']) for p in psutil.process_iter(['pid', 'name'])]
            processes.sort(key=lambda x: x[0].lower())
            all_processes = processes.copy()

            process_window = tk.Toplevel(self.root); process_window.title("בחר תהליך"); process_window.geometry("450x550")
            process_window.configure(bg='#1a1a1a'); process_window.attributes('-topmost', True)
            # ... (יצירת ווידג'טים בחלון - search, listbox, scrollbar, buttons) ...
            search_frame = tk.Frame(process_window, bg='#1a1a1a'); search_frame.pack(fill='x', padx=10, pady=10)
            tk.Label(search_frame, text="חיפוש:", font=("Arial", 10), fg="white", bg='#1a1a1a').pack(side='left', padx=5)
            search_var = tk.StringVar(); search_entry = tk.Entry(search_frame, textvariable=search_var, font=("Arial", 10), bg='#333333', fg='white', insertbackground='white'); search_entry.pack(side='left', fill='x', expand=True, padx=5); search_entry.focus()
            frame = tk.Frame(process_window, bg='#1a1a1a'); frame.pack(fill='both', expand=True, padx=10, pady=5)
            scrollbar = tk.Scrollbar(frame); scrollbar.pack(side='right', fill='y')
            listbox = tk.Listbox(frame, bg='#333333', fg='white', selectmode='single', yscrollcommand=scrollbar.set, font=("Arial", 10), selectbackground="#00ff00", selectforeground="black"); listbox.pack(side='left', fill='both', expand=True); scrollbar.config(command=listbox.yview)
            for proc_name, proc_pid in processes: listbox.insert('end', f"{proc_name} (PID: {proc_pid})")
            def filter_processes(*args): # Filter function
                search_term = search_var.get().lower(); listbox.delete(0, tk.END)
                for n, pid in all_processes:
                    if search_term in n.lower(): listbox.insert('end', f"{n} (PID: {pid})")
            search_var.trace('w', filter_processes)

            def on_select(event=None):
                """מטפל בבחירת תהליך."""
                if not listbox.curselection(): return
                selected_text = listbox.get(listbox.curselection()[0])
                try:
                    pid_str = selected_text.split('PID: ')[1].replace(')', '')
                    proc_pid = int(pid_str)
                    proc_name = selected_text.split(' (PID:')[0]

                    temp_handle = None # Handle זמני
                    try:
                        # 1. נקה Handle ישן
                        if self.process_handle:
                            try: win32api.CloseHandle(self.process_handle)
                            except Exception as close_err: print(f"Note: Ignored error closing previous handle: {close_err}")
                            finally: self.process_handle = None

                        # 2. פתח Handle חדש
                        temp_handle = win32api.OpenProcess(REQUIRED_ACCESS, False, proc_pid)
                        if not temp_handle: raise Exception("OpenProcess failed")

                        # 3. מצא כתובת בסיס
                        base_addr = get_module_base_address(temp_handle, GAME_MODULE_NAME)

                        # 4. עדכן משתני מחלקה
                        self.process_handle = temp_handle; self.selected_process = proc_pid; self.module_base = base_addr

                        # 5. עדכן GUI והודעות
                        if self.module_base:
                            self.process_label.config(text=f"נבחר: {proc_name} ({proc_pid}) | בסיס: {hex(self.module_base)}", fg="#00ff00")
                            messagebox.showinfo("הצלחה", f"'{proc_name}' נבחר וכתובת בסיס ({hex(self.module_base)}) נמצאה.")
                            process_window.destroy()
                        else:
                            self.process_label.config(text=f"נבחר: {proc_name} ({proc_pid}) | בסיס לא נמצא!", fg="#ffff00")
                            messagebox.showwarning("אזהרה", f"לא נמצא מודול '{GAME_MODULE_NAME}' בתהליך.\nודא שם ושהמשחק רץ. הפיצ'רים לא יעבדו.")

                    except Exception as open_error:
                        # ===> התיקון לשגיאה 1 <===
                        last_error = win32api.GetLastError()
                        error_msg = f"שגיאה בגישה לתהליך {proc_name} (PID: {proc_pid}).\n"
                        if last_error == ERROR_ACCESS_DENIED:
                           error_msg += f"שגיאת גישה (Error {ERROR_ACCESS_DENIED}).\nודא הרצת מנהל.\n"
                        else:
                           error_msg += f"פרטי שגיאה: {open_error}\n(קוד: {last_error})\n"
                        print(f"Error accessing process {proc_pid}: {open_error} (Code: {last_error})")
                        messagebox.showerror("שגיאה בפתיחת תהליך", error_msg)
                        # נסה לסגור את ה-Handle הזמני אם הוא נוצר לפני הכישלון
                        if temp_handle:
                             try:
                                 win32api.CloseHandle(temp_handle)
                             except Exception as close_err:
                                 print(f"Note: Error closing temp handle during error handling: {close_err}")
                        # איפוס משתנים
                        self.process_handle = None; self.selected_process = None; self.module_base = None
                        self.process_label.config(text="בחירת תהליך נכשלה", fg="#ff0000")
                        # ===> סוף התיקון לשגיאה 1 <===

                except (IndexError, ValueError) as parse_error:
                    messagebox.showerror("שגיאה", f"שגיאה בעיבוד בחירה: {parse_error}")

            listbox.bind("<Double-Button-1>", on_select)
            # ... (כפתורי בחירה/ביטול) ...
            button_frame = tk.Frame(process_window, bg='#1a1a1a'); button_frame.pack(fill='x', padx=10, pady=10)
            tk.Button(button_frame, text="בחר", command=on_select, font=("Arial", 10), bg='#333333', fg='white', activebackground='#00ff00', activeforeground='black', relief=tk.FLAT, width=10).pack(side='right', padx=5)
            tk.Button(button_frame, text="בטל", command=process_window.destroy, font=("Arial", 10), bg='#333333', fg='white', activebackground='#ff0000', activeforeground='black', relief=tk.FLAT, width=10).pack(side='right', padx=5)

        except Exception as e: messagebox.showerror("שגיאה", f"נכשל בקבלת רשימת תהליכים: {str(e)}")

    def set_current_weapon(self, weapon_id, weapon_name):
        """מנסה לכתוב ID נשק."""
        # ... (קוד זהה לקודם) ...
        feature = "current_weapon_id"; data_type = int; data_size = 4 # התאם למשחק!
        if not self.process_handle: messagebox.showerror("שגיאה", "בחר תהליך!"); return
        address = self.get_feature_address(feature)
        if address is None: return
        try:
            if write_memory(self.process_handle, address, weapon_id, data_type, data_size):
                 messagebox.showinfo("הצלחה", f"ניסיון להחליף ל-{weapon_name} (ID: {weapon_id}) הצליח.")
            else: messagebox.showerror("שגיאה בכתיבה", f"נכשל בכתיבת ID נשק {weapon_id}. (שגיאה: {win32api.GetLastError()})")
        except Exception as e: messagebox.showerror("שגיאה קריטית", f"שגיאה בהחלפת נשק: {str(e)}")


    def browse_dll(self):
        """דיאלוג בחירת DLL."""
        # ... (קוד זהה לקודם) ...
        filepath = filedialog.askopenfilename(title="בחר DLL", filetypes=(("DLL", "*.dll"), ("All", "*.*")))
        if filepath: self.dll_path.set(filepath)

    def inject_dll_threaded(self):
        """מתחיל הזרקת DLL ב-Thread."""
        # ... (קוד זהה לקודם) ...
        if not self.process_handle: messagebox.showerror("שגיאה", "בחר תהליך!"); return
        dll_to_inject = self.dll_path.get()
        if not dll_to_inject or not os.path.exists(dll_to_inject): messagebox.showerror("שגיאה", f"DLL לא נמצא:\n{dll_to_inject}"); return
        threading.Thread(target=self.inject_dll_logic, args=(self.process_handle, dll_to_inject), daemon=True).start()
        messagebox.showinfo("הזרקה", "הזרקת DLL החלה ברקע...")


    def inject_dll_logic(self, process_handle_local, dll_path):
        """הלוגיקה של הזרקת DLL."""
        remote_memory = None; thread_handle = None; kernel32 = None; load_library_addr = None
        try:
            # ... (קוד הקצאה, כתיבה, קבלת LoadLibraryA, יצירת Thread, המתנה - כמו קודם) ...
            if not process_handle_local: raise Exception("Process handle invalid.")
            if not os.path.exists(dll_path): raise FileNotFoundError(f"DLL not found: {dll_path}")
            path_bytes = (dll_path + '\0').encode('utf-8'); path_size = len(path_bytes)
            remote_memory = win32process.VirtualAllocEx(process_handle_local, 0, path_size, win32con.MEM_COMMIT | win32con.MEM_RESERVE, win32con.PAGE_READWRITE)
            if not remote_memory: raise Exception(f"VirtualAllocEx failed: {win32api.GetLastError()}")
            bytes_written = ctypes.c_size_t()
            if not win32process.WriteProcessMemory(process_handle_local, remote_memory, path_bytes, path_size, ctypes.byref(bytes_written)) or bytes_written.value != path_size: raise Exception(f"WriteProcessMemory failed: {win32api.GetLastError()}")
            kernel32 = win32api.GetModuleHandle('kernel32.dll')
            load_library_addr = win32api.GetProcAddress(kernel32, 'LoadLibraryA')
            if not load_library_addr: raise Exception(f"GetProcAddress failed: {win32api.GetLastError()}")
            thread_handle, thread_id = win32process.CreateRemoteThread(process_handle_local, None, 0, load_library_addr, remote_memory, 0, None)
            if not thread_handle: raise Exception(f"CreateRemoteThread failed: {win32api.GetLastError()}")
            wait_result = win32event.WaitForSingleObject(thread_handle, 15000)
            if wait_result == win32event.WAIT_TIMEOUT: raise Exception("Remote thread timed out.")
            elif wait_result != win32event.WAIT_OBJECT_0: raise Exception(f"WaitForSingleObject failed: {win32api.GetLastError()}")
            # --- הודעה לתור ---
            self.gui_queue.put(("messagebox", "הצלחה", "DLL הוזרק בהצלחה!"))
        except FileNotFoundError as fnf_error:
            self.gui_queue.put(("errorbox", "שגיאת הזרקה", str(fnf_error)))
        except Exception as e:
            last_error = win32api.GetLastError()
            error_details = f"נכשל בהזרקת DLL: {str(e)}\n(קוד: {last_error})"
            self.gui_queue.put(("errorbox", "שגיאת הזרקה", error_details))
        finally:
            # ===> התיקון לשגיאה 2 <===
            # סגירת ה-handle של ה-thread
            if thread_handle:
                try:
                    win32api.CloseHandle(thread_handle)
                except Exception as e_thread:
                    print(f"Note: Error closing thread handle: {e_thread}")
            # שחרור הזיכרון שהוקצה בתהליך המטרה
            if remote_memory and process_handle_local:
                try:
                    win32process.VirtualFreeEx(process_handle_local, remote_memory, 0, win32con.MEM_RELEASE)
                except Exception as e_mem:
                    print(f"Note: Error freeing remote memory: {e_mem}")
            # ===> סוף התיקון לשגיאה 2 <===

    def on_closing(self):
        """משחרר משאבים לפני סגירה."""
        print("Closing application...")
        if self.process_handle:
            try:
                win32api.CloseHandle(self.process_handle)
            except Exception as e:
                print(f"Error closing handle on exit: {e}")
        self.root.destroy()

    def run(self):
        """מריץ את ה-GUI."""
        self.root.mainloop()

# ================== נקודת הכניסה הראשית ==================
if __name__ == "__main__":
    # ... (בדיקות הרשאות, VM, הסתרת קונסול - כמו קודם) ...
    is_admin = False
    try: is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    except: print("Could not check admin status."); is_admin = False
    if not is_admin: messagebox.showerror("נדרשות הרשאות", "יש להריץ כמנהל."); sys.exit(1)
    if is_running_in_vm():
        if not messagebox.askyesno("אזהרה - VM", "זוהתה סביבה וירטואלית.\nלהמשיך?"): sys.exit(1)
        else: print("Proceeding in VM environment.")
    hide_console_window()
    # ... (יצירת מופע והרצה) ...
    menu = EnhancedModMenu()
    menu.run()