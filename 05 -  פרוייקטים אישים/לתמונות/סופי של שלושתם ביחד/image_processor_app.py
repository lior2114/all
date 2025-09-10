import os
import json
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import tkinter
from tkinter import Tk, filedialog, Toplevel, Label, Entry, Button, StringVar, END, messagebox, ttk, Frame, font, Canvas, Scrollbar
from tkinter.ttk import Notebook, Style
import shutil
import time

# קובץ הגדרות
CONFIG_FILE_NAME = "image_settings.json"

class ImageProcessorApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("🎨 מעבד תמונות מקצועי")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        
        # הגדרת גודל מינימלי לחלון - קומפקטי יותר
        self.root.minsize(700, 500)
        
        # הגדרת התנהגות resize
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # הגדרת סגנון
        self.setup_styles()
        
        # יצירת header
        self.create_header()
        
        # יצירת notebook עם tabs
        self.notebook = Notebook(self.root, style='Custom.TNotebook')
        self.notebook.pack(fill='both', expand=True, padx=20, pady=(0, 20))
        
        # הגדרת התנהגות resize ל-notebook
        self.notebook.grid_rowconfigure(0, weight=1)
        self.notebook.grid_columnconfigure(0, weight=1)
        
        # הגדרת תמיכה ב-RTL ומיזוז למרכז
        self.setup_rtl_and_center()
        
        # יצירת tabs
        self.create_rename_tab()
        self.create_all_files_tab()
        self.create_selected_files_tab()
    
    def setup_rtl_and_center(self):
        """הגדרת תמיכה ב-RTL ומיזוז למרכז"""
        # הגדרת כיוון RTL
        self.rtl_anchor = 'e'  # east (ימין)
        self.rtl_justify = 'right'
        self.rtl_side = 'right'
    
    def setup_styles(self):
        """הגדרת סגנונות מותאמים אישית"""
        self.style = Style()
        
        # צבעים
        self.colors = {
            'primary': '#2c3e50',
            'secondary': '#3498db',
            'success': '#27ae60',
            'warning': '#f39c12',
            'danger': '#e74c3c',
            'light': '#ecf0f1',
            'dark': '#34495e',
            'white': '#ffffff',
            'gray': '#95a5a6'
        }
        
        # הגדרת סגנון ל-Notebook
        self.style.configure('Custom.TNotebook', 
                           background=self.colors['light'],
                           borderwidth=0)
        self.style.configure('Custom.TNotebook.Tab',
                           background=self.colors['white'],
                           foreground=self.colors['primary'],
                           padding=[20, 10],
                           font=('Arial', 12, 'bold'))
        self.style.map('Custom.TNotebook.Tab',
                      background=[('selected', self.colors['secondary']),
                                ('active', self.colors['light'])],
                      foreground=[('selected', self.colors['white']),
                                ('active', self.colors['primary'])])
    
    def create_header(self):
        """יצירת header יפה לאפליקציה"""
        header_frame = Frame(self.root, bg=self.colors['primary'], height=80)
        header_frame.pack(fill='x', padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # כותרת ראשית
        title_label = Label(header_frame, 
                          text="🎨 מעבד תמונות מקצועי",
                          font=('Arial', 24, 'bold'),
                          fg=self.colors['white'],
                          bg=self.colors['primary'])
        title_label.pack(expand=True)
        
        # תת-כותרת
        subtitle_label = Label(header_frame,
                             text="כלי מתקדם לעיבוד ושינוי שמות תמונות",
                             font=('Arial', 12),
                             fg=self.colors['light'],
                             bg=self.colors['primary'])
        subtitle_label.pack()
        
    def create_rename_tab(self):
        """יצירת tab לשינוי שמות קבצים פשוט"""
        rename_frame = Frame(self.notebook, bg=self.colors['white'])
        self.notebook.add(rename_frame, text="📁 שינוי שמות קבצים")
        
        # משתנים
        self.rename_directory_var = StringVar()
        self.rename_custom_var = StringVar()
        self.rename_date_var = StringVar()
        
        # יצירת container מרכזי עם scrollbar
        canvas = tkinter.Canvas(rename_frame, bg=self.colors['white'])
        scrollbar = tkinter.Scrollbar(rename_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg=self.colors['white'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        scrollbar.pack(side="right", fill="y")
        
        # הוספת תמיכה בגלילה עם העכבר
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        main_container = scrollable_frame
        
        # כותרת
        title_frame = Frame(main_container, bg=self.colors['white'])
        title_frame.pack(fill='x', pady=(0, 15), padx=40)
        
        Label(title_frame, text="📁 שינוי שמות קבצים פשוט", 
              font=("Arial", 14, "bold"), 
              fg=self.colors['primary'], 
              bg=self.colors['white']).pack(anchor='center')
        
        Label(title_frame, text="שינוי שמות קבצים ללא עיבוד תמונות", 
              font=("Arial", 9), 
              fg=self.colors['gray'], 
              bg=self.colors['white']).pack(anchor='center')
        
        # יצירת form container
        form_container = Frame(main_container, bg=self.colors['white'])
        form_container.pack(expand=True, fill='both')
        
        # תיקייה
        self.create_form_field(form_container, "📂 תיקייה:", self.rename_directory_var, 
                              self.browse_rename_directory, "בחר תיקייה עם קבצי תמונה")
        
        # שם בסיס
        self.create_form_field(form_container, "🏷️ שם בסיס:", self.rename_custom_var, 
                              None, "הזן שם בסיס לקבצים")
        
        # תאריך
        self.create_form_field(form_container, "📅 תאריך:", self.rename_date_var, 
                              None, "הזן תאריך (למשל: 2024-01-15)")
        
        # כפתור אישור
        button_frame = Frame(form_container, bg=self.colors['white'])
        button_frame.pack(fill='x', pady=12)
        
        self.create_button(button_frame, "🚀 התחל שינוי שמות", 
                          self.rename_files_simple, self.colors['success'])
        
        # תווית תוצאה
        self.rename_result_label = Label(form_container, text="", 
                                        font=("Arial", 11), 
                                        bg=self.colors['white'])
        self.rename_result_label.pack(pady=10)
    
    def create_form_field(self, parent, label_text, var, browse_command, placeholder=""):
        """יצירת שדה form יפה וקומפקטי עם RTL מסודר"""
        field_frame = Frame(parent, bg=self.colors['white'])
        field_frame.pack(fill='x', pady=4, padx=40)  # padding משני הצדדים
        
        # תווית - מיושרת לימין
        label = Label(field_frame, text=label_text, 
                     font=("Arial", 10, "bold"),
                     fg=self.colors['primary'], 
                     bg=self.colors['white'])
        label.pack(anchor='e', pady=(0, 2))  # יישור לימין פשוט
        
        # שדה קלט וכפתור - מסודר מימין לשמאל
        input_frame = Frame(field_frame, bg=self.colors['white'])
        input_frame.pack(fill='x')
        
        # כפתור בחירה (אם קיים) - מימין
        if browse_command:
            button = Button(input_frame, text="📁 בחר", 
                           command=browse_command,
                           font=("Arial", 8, "bold"),
                           bg=self.colors['secondary'],
                           fg=self.colors['white'],
                           relief='flat',
                           padx=12,
                           pady=3)
            button.pack(side='right', padx=(3, 0))
        
        # שדה קלט - משמאל לכפתור
        entry = Entry(input_frame, textvariable=var, 
                     font=("Arial", 9),
                     relief='solid', 
                     bd=1,
                     bg=self.colors['white'],
                     justify='right')  # יישור טקסט לימין
        entry.pack(side='left', fill='x', expand=True)
        
        # placeholder - רק אם השדה ריק
        if placeholder:
            def on_focus_in(event):
                if entry.get() == placeholder:
                    entry.delete(0, END)
                    entry.config(fg='black')
            
            def on_focus_out(event):
                if not entry.get():
                    entry.insert(0, placeholder)
                    entry.config(fg='gray')
            
            # בדיקה אם השדה כבר יש לו ערך
            if not var.get():
                entry.insert(0, placeholder)
                entry.config(fg='gray')
            
            entry.bind('<FocusIn>', on_focus_in)
            entry.bind('<FocusOut>', on_focus_out)
    
    def create_button(self, parent, text, command, color):
        """יצירת כפתור יפה וקומפקטי עם RTL"""
        button = Button(parent, text=text, 
                       command=command,
                       font=("Arial", 11, "bold"),
                       bg=color,
                       fg=self.colors['white'],
                       relief='flat',
                       padx=20,
                       pady=6,
                       cursor='hand2')
        button.pack(anchor='center', pady=3)
        
        # אפקט hover
        def on_enter(e):
            button.config(bg=self.darken_color(color))
        def on_leave(e):
            button.config(bg=color)
        
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
    
    def darken_color(self, color):
        """הכהיית צבע"""
        color_map = {
            self.colors['success']: '#229954',
            self.colors['secondary']: '#2980b9',
            self.colors['warning']: '#e67e22',
            self.colors['danger']: '#c0392b'
        }
        return color_map.get(color, color)
        
    def create_all_files_tab(self):
        """יצירת tab לעיבוד כל הקבצים בתיקייה"""
        all_files_frame = Frame(self.notebook, bg=self.colors['white'])
        self.notebook.add(all_files_frame, text="🖼️ עיבוד כל הקבצים")
        
        # טעינת הגדרות
        settings = self.load_settings()
        
        # משתנים
        self.all_source_var = StringVar()
        self.all_dest_var = StringVar()
        self.all_custom_var = StringVar()
        self.all_date_var = StringVar()
        self.all_overlay_var = StringVar(value=settings["all_files_overlay_path"])
        self.all_width_var = StringVar(value=str(settings["overlay_width"]))
        self.all_height_var = StringVar(value=str(settings["overlay_height"]))
        self.all_margin_top_var = StringVar(value=str(settings["margin_top"]))
        self.all_margin_right_var = StringVar(value=str(settings["margin_right"]))
        
        # יצירת container מרכזי עם scrollbar
        canvas = Canvas(all_files_frame, bg=self.colors['white'])
        scrollbar = Scrollbar(all_files_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg=self.colors['white'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        scrollbar.pack(side="right", fill="y")
        
        # הוספת תמיכה בגלילה עם העכבר - גרסה משופרת
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        # bind ל-canvas עצמו במקום bind_all
        canvas.bind("<MouseWheel>", _on_mousewheel)
        canvas.bind("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))
        canvas.bind("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))
        
        # focus ל-canvas כדי שיקבל אירועי עכבר
        canvas.focus_set()
        
        # bind גם ל-scrollable_frame
        def _on_frame_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        scrollable_frame.bind("<MouseWheel>", _on_frame_mousewheel)
        scrollable_frame.bind("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))
        scrollable_frame.bind("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))
        
        main_container = scrollable_frame
        
        # כותרת
        title_frame = Frame(main_container, bg=self.colors['white'])
        title_frame.pack(fill='x', pady=(0, 15), padx=40)
        
        Label(title_frame, text="🖼️ עיבוד כל התמונות בתיקייה", 
              font=("Arial", 14, "bold"), 
              fg=self.colors['primary'], 
              bg=self.colors['white']).pack(anchor='center')
        
        Label(title_frame, text="עיבוד כל התמונות בתיקייה עם שכבת-על מתקדמת", 
              font=("Arial", 9), 
              fg=self.colors['gray'], 
              bg=self.colors['white']).pack(anchor='center')
        
        # יצירת form container
        form_container = Frame(main_container, bg=self.colors['white'])
        form_container.pack(expand=True, fill='both')
        
        # תיקיית מקור
        self.create_form_field(form_container, "📂 תיקיית מקור:", self.all_source_var, 
                              self.browse_all_source, "בחר תיקייה עם תמונות")
        
        # תיקיית יעד
        self.create_form_field(form_container, "📁 תיקיית יעד:", self.all_dest_var, 
                              self.browse_all_dest, "בחר תיקייה לשמירת התמונות המעובדות")
        
        # שם בסיס
        self.create_form_field(form_container, "🏷️ שם בסיס:", self.all_custom_var, 
                              None, "הזן שם בסיס לקבצים")
        
        # תאריך
        self.create_form_field(form_container, "📅 תאריך:", self.all_date_var, 
                              None, "הזן תאריך (למשל: 2024-01-15)")
        
        # קובץ שכבת-על
        overlay_placeholder = "בחר תמונה לשכבת-על" if not settings["all_files_overlay_path"] else ""
        self.create_form_field(form_container, "🎨 קובץ שכבת-על:", self.all_overlay_var, 
                              self.browse_all_overlay, overlay_placeholder)
        
        # הגדרות גודל וריווח - פריסה מסודרת
        settings_frame = Frame(form_container, bg=self.colors['white'])
        settings_frame.pack(fill='x', pady=8, padx=40)
        
        Label(settings_frame, text="⚙️ הגדרות שכבת-על", 
              font=("Arial", 11, "bold"), 
              fg=self.colors['primary'], 
              bg=self.colors['white']).pack(anchor='center', pady=(0, 8))
        
        # גודל וריווח בשורה אחת
        settings_input_frame = Frame(settings_frame, bg=self.colors['white'])
        settings_input_frame.pack(anchor='center', pady=2)
        
        # גודל
        size_frame = Frame(settings_input_frame, bg=self.colors['white'])
        size_frame.pack(side='right', padx=(0, 30))
        
        Label(size_frame, text="📏 גודל:", 
              font=("Arial", 9, "bold"), 
              fg=self.colors['primary'], 
              bg=self.colors['white']).pack(anchor='center')
        
        size_inputs = Frame(size_frame, bg=self.colors['white'])
        size_inputs.pack(pady=2)
        
        # סידור השדות מימין לשמאל
        Entry(size_inputs, textvariable=self.all_height_var, 
              font=("Arial", 8), width=6, relief='solid', bd=1,
              justify='right').pack(side='right', padx=2)
        Label(size_inputs, text="גובה:", 
              font=("Arial", 8), 
              fg=self.colors['dark'], 
              bg=self.colors['white']).pack(side='right')
        
        Entry(size_inputs, textvariable=self.all_width_var, 
              font=("Arial", 8), width=6, relief='solid', bd=1,
              justify='right').pack(side='right', padx=(8, 2))
        Label(size_inputs, text="רוחב:", 
              font=("Arial", 8), 
              fg=self.colors['dark'], 
              bg=self.colors['white']).pack(side='right')
        
        # ריווח
        margin_frame = Frame(settings_input_frame, bg=self.colors['white'])
        margin_frame.pack(side='right')
        
        Label(margin_frame, text="📐 ריווח:", 
              font=("Arial", 9, "bold"), 
              fg=self.colors['primary'], 
              bg=self.colors['white']).pack(anchor='center')
        
        margin_inputs = Frame(margin_frame, bg=self.colors['white'])
        margin_inputs.pack(pady=2)
        
        # סידור השדות מימין לשמאל
        Entry(margin_inputs, textvariable=self.all_margin_right_var, 
              font=("Arial", 8), width=6, relief='solid', bd=1,
              justify='right').pack(side='right', padx=2)
        Label(margin_inputs, text="מימין:", 
              font=("Arial", 8), 
              fg=self.colors['dark'], 
              bg=self.colors['white']).pack(side='right')
        
        Entry(margin_inputs, textvariable=self.all_margin_top_var, 
              font=("Arial", 8), width=6, relief='solid', bd=1,
              justify='right').pack(side='right', padx=(8, 2))
        Label(margin_inputs, text="מלמעלה:", 
              font=("Arial", 8), 
              fg=self.colors['dark'], 
              bg=self.colors['white']).pack(side='right')
        
        # כפתור אישור
        button_frame = Frame(form_container, bg=self.colors['white'])
        button_frame.pack(fill='x', pady=12)
        
        self.create_button(button_frame, "🚀 התחל עיבוד כל הקבצים", 
                          self.process_all_files, self.colors['secondary'])
        
        # תווית תוצאה
        self.all_result_label = Label(form_container, text="", 
                                     font=("Arial", 11), 
                                     bg=self.colors['white'])
        self.all_result_label.pack(pady=10)
        
        # הוספת bind לכל ה-widgets בתוך ה-frame
        def bind_mousewheel_to_widgets(widget):
            widget.bind("<MouseWheel>", _on_frame_mousewheel)
            widget.bind("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))
            widget.bind("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))
            for child in widget.winfo_children():
                bind_mousewheel_to_widgets(child)
        
        # bind לכל ה-widgets
        bind_mousewheel_to_widgets(main_container)
        
    def create_selected_files_tab(self):
        """יצירת tab לעיבוד קבצים נבחרים"""
        selected_frame = Frame(self.notebook, bg=self.colors['white'])
        self.notebook.add(selected_frame, text="🎯 עיבוד קבצים נבחרים")
        
        # טעינת הגדרות
        settings = self.load_settings()
        
        # משתנים
        self.selected_source_var = StringVar()
        self.selected_dest_var = StringVar()
        self.selected_custom_var = StringVar()
        self.selected_date_var = StringVar()
        self.selected_overlay_var = StringVar(value=settings["selected_files_overlay_path"])
        self.selected_width_var = StringVar(value=str(settings["overlay_width"]))
        self.selected_height_var = StringVar(value=str(settings["overlay_height"]))
        self.selected_margin_top_var = StringVar(value=str(settings["margin_top"]))
        self.selected_margin_right_var = StringVar(value=str(settings["margin_right"]))
        
        # יצירת container מרכזי עם scrollbar
        canvas = Canvas(selected_frame, bg=self.colors['white'])
        scrollbar = Scrollbar(selected_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg=self.colors['white'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        scrollbar.pack(side="right", fill="y")
        
        # הוספת תמיכה בגלילה עם העכבר
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        main_container = scrollable_frame
        
        # כותרת
        title_frame = Frame(main_container, bg=self.colors['white'])
        title_frame.pack(fill='x', pady=(0, 15), padx=40)
        
        Label(title_frame, text="🎯 עיבוד תמונות נבחרות", 
              font=("Arial", 14, "bold"), 
              fg=self.colors['primary'], 
              bg=self.colors['white']).pack(anchor='center')
        
        Label(title_frame, text="עיבוד תמונות נבחרות עם שכבת-על", 
              font=("Arial", 9), 
              fg=self.colors['gray'], 
              bg=self.colors['white']).pack(anchor='center')
        
        # יצירת form container
        form_container = Frame(main_container, bg=self.colors['white'])
        form_container.pack(expand=True, fill='both')
        
        # קבצי מקור
        self.create_form_field(form_container, "🖼️ קבצי מקור:", self.selected_source_var, 
                              self.browse_selected_source, "בחר תמונות לעיבוד (Ctrl+Click לבחירה מרובה)")
        
        # תיקיית יעד
        self.create_form_field(form_container, "📁 תיקיית יעד:", self.selected_dest_var, 
                              self.browse_selected_dest, "בחר תיקייה לשמירת התמונות המעובדות")
        
        # שם בסיס
        self.create_form_field(form_container, "🏷️ שם בסיס:", self.selected_custom_var, 
                              None, "הזן שם בסיס לקבצים")
        
        # תאריך
        self.create_form_field(form_container, "📅 תאריך:", self.selected_date_var, 
                              None, "הזן תאריך (למשל: 2024-01-15)")
        
        # קובץ שכבת-על
        overlay_placeholder = "בחר תמונה לשכבת-על" if not settings["selected_files_overlay_path"] else ""
        self.create_form_field(form_container, "🎨 קובץ שכבת-על:", self.selected_overlay_var, 
                              self.browse_selected_overlay, overlay_placeholder)
        
        # הגדרות גודל וריווח - פריסה מסודרת
        settings_frame = Frame(form_container, bg=self.colors['white'])
        settings_frame.pack(fill='x', pady=8, padx=40)
        
        Label(settings_frame, text="⚙️ הגדרות שכבת-על", 
              font=("Arial", 11, "bold"), 
              fg=self.colors['primary'], 
              bg=self.colors['white']).pack(anchor='center', pady=(0, 8))
        
        # גודל וריווח בשורה אחת
        settings_input_frame = Frame(settings_frame, bg=self.colors['white'])
        settings_input_frame.pack(anchor='center', pady=2)
        
        # גודל
        size_frame = Frame(settings_input_frame, bg=self.colors['white'])
        size_frame.pack(side='right', padx=(0, 30))
        
        Label(size_frame, text="📏 גודל:", 
              font=("Arial", 9, "bold"), 
              fg=self.colors['primary'], 
              bg=self.colors['white']).pack(anchor='center')
        
        size_inputs = Frame(size_frame, bg=self.colors['white'])
        size_inputs.pack(pady=2)
        
        # סידור השדות מימין לשמאל
        Entry(size_inputs, textvariable=self.selected_height_var, 
              font=("Arial", 8), width=6, relief='solid', bd=1,
              justify='right').pack(side='right', padx=2)
        Label(size_inputs, text="גובה:", 
              font=("Arial", 8), 
              fg=self.colors['dark'], 
              bg=self.colors['white']).pack(side='right')
        
        Entry(size_inputs, textvariable=self.selected_width_var, 
              font=("Arial", 8), width=6, relief='solid', bd=1,
              justify='right').pack(side='right', padx=(8, 2))
        Label(size_inputs, text="רוחב:", 
              font=("Arial", 8), 
              fg=self.colors['dark'], 
              bg=self.colors['white']).pack(side='right')
        
        # ריווח
        margin_frame = Frame(settings_input_frame, bg=self.colors['white'])
        margin_frame.pack(side='right')
        
        Label(margin_frame, text="📐 ריווח:", 
              font=("Arial", 9, "bold"), 
              fg=self.colors['primary'], 
              bg=self.colors['white']).pack(anchor='center')
        
        margin_inputs = Frame(margin_frame, bg=self.colors['white'])
        margin_inputs.pack(pady=2)
        
        # סידור השדות מימין לשמאל
        Entry(margin_inputs, textvariable=self.selected_margin_right_var, 
              font=("Arial", 8), width=6, relief='solid', bd=1,
              justify='right').pack(side='right', padx=2)
        Label(margin_inputs, text="מימין:", 
              font=("Arial", 8), 
              fg=self.colors['dark'], 
              bg=self.colors['white']).pack(side='right')
        
        Entry(margin_inputs, textvariable=self.selected_margin_top_var, 
              font=("Arial", 8), width=6, relief='solid', bd=1,
              justify='right').pack(side='right', padx=(8, 2))
        Label(margin_inputs, text="מלמעלה:", 
              font=("Arial", 8), 
              fg=self.colors['dark'], 
              bg=self.colors['white']).pack(side='right')
        
        # כפתור אישור
        button_frame = Frame(form_container, bg=self.colors['white'])
        button_frame.pack(fill='x', pady=12)
        
        self.create_button(button_frame, "🚀 התחל עיבוד קבצים נבחרים", 
                          self.process_selected_files, self.colors['warning'])
        
        # תווית תוצאה
        self.selected_result_label = Label(form_container, text="", 
                                          font=("Arial", 11), 
                                          bg=self.colors['white'])
        self.selected_result_label.pack(pady=10)
    
    # פונקציות עזר לבחירת קבצים
    def browse_rename_directory(self):
        path = filedialog.askdirectory(title="בחר תיקייה עם קבצי תמונה")
        if path:
            self.rename_directory_var.set(path)
    
    def browse_all_source(self):
        path = filedialog.askdirectory(title="בחר תיקיית מקור")
        if path:
            self.all_source_var.set(path)
    
    def browse_all_dest(self):
        path = filedialog.askdirectory(title="בחר תיקיית יעד")
        if path:
            self.all_dest_var.set(path)
    
    def browse_all_overlay(self):
        path = filedialog.askopenfilename(
            title="בחר קובץ שכבת-על לעיבוד כל הקבצים",
            filetypes=[
                ("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.PNG;*.JPG;*.JPEG;*.GIF;*.BMP"),
                ("All files", "*.*")
            ]
        )
        if path:
            self.all_overlay_var.set(path)
    
    def browse_selected_source(self):
        paths = filedialog.askopenfilenames(
            title="בחר תמונות (Ctrl+Click לבחירה מרובה)",
            filetypes=[
                ("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.PNG;*.JPG;*.JPEG;*.GIF;*.BMP"),
                ("All files", "*.*")
            ]
        )
        if paths:
            self.selected_source_var.set(";".join(paths))
    
    def browse_selected_dest(self):
        path = filedialog.askdirectory(title="בחר תיקיית יעד")
        if path:
            self.selected_dest_var.set(path)
    
    def browse_selected_overlay(self):
        path = filedialog.askopenfilename(
            title="בחר קובץ שכבת-על לקבצים נבחרים",
            filetypes=[
                ("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.PNG;*.JPG;*.JPEG;*.GIF;*.BMP"),
                ("All files", "*.*")
            ]
        )
        if path:
            self.selected_overlay_var.set(path)
    
    # פונקציות עיבוד
    def rename_files_simple(self):
        """שינוי שמות קבצים פשוט - מהקובץ change_name_in_files.py"""
        if not all([self.rename_directory_var.get(), self.rename_custom_var.get(), self.rename_date_var.get()]):
            self.rename_result_label.config(text="יש למלא את כל השדות", fg="red")
            return
        
        try:
            directory_path = self.rename_directory_var.get()
            custom_name = self.rename_custom_var.get()
            date = self.rename_date_var.get()
            base_name = "ארכיון - תמונה מס' "
            
            # Get all files in the directory
            files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
            
            # Filter for image files
            image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.PNG', '.JPG', '.JPEG', '.GIF', '.BMP']
            image_files = [f for f in files if any(f.lower().endswith(ext.lower()) for ext in image_extensions)]
            
            if not image_files:
                self.rename_result_label.config(text="לא נמצאו קבצי תמונה בתיקייה הנבחרת.", fg="red")
                return
            
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
                    continue

                try:
                    # שימוש ב-shutil במקום os.rename לבטיחות רבה יותר
                    shutil.move(old_file, new_file)
                except Exception as error_msg:
                    print(f"שגיאה בעת שינוי שם הקובץ {filename}: {error_msg}")
            
            self.rename_result_label.config(text=f"✅ הושלם בהצלחה! עובדו {len(image_files)} קבצים", 
                                          fg=self.colors['success'], font=("Arial", 12, "bold"))
            
        except Exception as error_msg:
            self.rename_result_label.config(text=f"❌ אירעה שגיאה: {error_msg}", 
                                          fg=self.colors['danger'], font=("Arial", 12, "bold"))
    
    def process_all_files(self):
        """עיבוד כל הקבצים - מהקובץ picture_all_file_selected.py"""
        if not all([self.all_source_var.get(), self.all_dest_var.get(), self.all_custom_var.get(), 
                   self.all_date_var.get(), self.all_overlay_var.get()]):
            self.all_result_label.config(text="⚠️ יש למלא את כל השדות", 
                                       fg=self.colors['danger'], font=("Arial", 12, "bold"))
            return
        
        # בדיקת תקינות גודל וריווח
        try:
            width = int(self.all_width_var.get())
            height = int(self.all_height_var.get())
            margin_top = int(self.all_margin_top_var.get())
            margin_right = int(self.all_margin_right_var.get())
            
            if width <= 0 or height <= 0:
                self.all_result_label.config(text="גודל חייב להיות מספר חיובי", fg="red")
                return
            if margin_top < 0 or margin_right < 0:
                self.all_result_label.config(text="ריווח חייב להיות מספר לא שלילי", fg="red")
                return
        except ValueError:
            self.all_result_label.config(text="נא להזין מספרים תקינים", fg="red")
            return
        
        # שמירת הגדרות לטאב "כל הקבצים"
        self.save_settings(self.all_overlay_var.get(), width, height, margin_top, margin_right, "all")
        
        # ספירת קבצים לעיבוד
        try:
            files = os.listdir(self.all_source_var.get())
            image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
            total_files = len(image_files)
        except:
            total_files = 0
        
        if total_files > 0:
            # יצירת פונקציית callback לעיבוד
            def process_callback(progress_var, progress_bar, status_label, is_cancelled_func):
                self.rename_images_all(self.all_source_var.get(), self.all_dest_var.get(), 
                                     "ארכיון - תמונה מס' ", self.all_custom_var.get(), self.all_date_var.get(),
                                     self.all_overlay_var.get(), width, height, margin_top, margin_right,
                                     progress_var, progress_bar, status_label, is_cancelled_func)
            
            # הצגת חלון progress
            cancelled = self.show_progress_window(total_files, process_callback)
            
            if not cancelled:
                self.all_result_label.config(text="✅ העיבוד הושלם בהצלחה!", 
                                           fg=self.colors['success'], font=("Arial", 12, "bold"))
            else:
                self.all_result_label.config(text="העיבוד בוטל על ידי המשתמש", fg="orange")
        else:
            self.all_result_label.config(text="לא נמצאו קבצי תמונה לעיבוד", fg="red")
    
    def process_selected_files(self):
        """עיבוד קבצים נבחרים - מהקובץ picture_selected.py"""
        if not all([self.selected_source_var.get(), self.selected_dest_var.get(), 
                   self.selected_custom_var.get(), self.selected_date_var.get(), self.selected_overlay_var.get()]):
            self.selected_result_label.config(text="⚠️ יש למלא את כל השדות", 
                                            fg=self.colors['danger'], font=("Arial", 12, "bold"))
            return
        
        # בדיקת תקינות גודל וריווח
        try:
            width = int(self.selected_width_var.get())
            height = int(self.selected_height_var.get())
            margin_top = int(self.selected_margin_top_var.get())
            margin_right = int(self.selected_margin_right_var.get())
            
            if width <= 0 or height <= 0:
                self.selected_result_label.config(text="⚠️ גודל חייב להיות מספר חיובי", 
                                                fg=self.colors['danger'], font=("Arial", 12, "bold"))
                return
            if margin_top < 0 or margin_right < 0:
                self.selected_result_label.config(text="⚠️ ריווח חייב להיות מספר לא שלילי", 
                                                fg=self.colors['danger'], font=("Arial", 12, "bold"))
                return
        except ValueError:
            self.selected_result_label.config(text="⚠️ נא להזין מספרים תקינים", 
                                            fg=self.colors['danger'], font=("Arial", 12, "bold"))
            return
        
        # שמירת הגדרות לטאב "קבצים נבחרים"
        self.save_settings(self.selected_overlay_var.get(), width, height, margin_top, margin_right, "selected")
        
        try:
            source_files_str = self.selected_source_var.get()
            source_files = source_files_str.split(";") if source_files_str else []
            
            self.rename_images_selected(source_files, self.selected_dest_var.get(),
                                      "ארכיון - תמונה מס' ", self.selected_custom_var.get(), 
                                      self.selected_date_var.get(), self.selected_overlay_var.get(),
                                      width, height, margin_top, margin_right)
            
            self.selected_result_label.config(text=f"✅ הושלם בהצלחה! עובדו {len(source_files)} קבצים", 
                                            fg=self.colors['success'], font=("Arial", 12, "bold"))
            
        except Exception as error_msg:
            self.selected_result_label.config(text=f"❌ אירעה שגיאה: {error_msg}", 
                                            fg=self.colors['danger'], font=("Arial", 12, "bold"))
    
    # פונקציות עיבוד תמונות (מהקבצים המקוריים)
    def rename_images_all(self, source_directory, destination_directory, base_name, custom_name, date, 
                         overlay_image_path, overlay_width, overlay_height, margin_top, margin_right,
                         progress_var=None, progress_bar=None, status_label=None, is_cancelled_func=None):
        """עיבוד כל התמונות בתיקייה - מהקובץ picture_all_file_selected.py"""
        try:
            # Get list of files in the source directory
            files = os.listdir(source_directory)
            # Filter out only image files
            image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
            # Sort files to ensure consistent numbering
            image_files.sort()

            # Load the overlay image
            overlay_image = Image.open(overlay_image_path).convert("RGBA")
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
                    continue

                try:
                    # Open the original image
                    original_image = Image.open(old_file).convert("RGBA")

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

                    # Save the modified image with the new name
                    combined_image.save(new_file)
                except Exception as processing_error:
                    print(f"Error processing file {filename}: {processing_error}")
            
            # עדכון סיום
            if status_label:
                status_label.config(text="העיבוד הושלם!")

        except FileNotFoundError:
            print("Error: Directory or overlay image not found.")
        except Exception as general_error:
            print(f"An error occurred: {general_error}")
    
    def rename_images_selected(self, source_files, destination_directory, base_name, custom_name, date, 
                              overlay_image_path, overlay_width, overlay_height, margin_top, margin_right):
        """עיבוד תמונות נבחרות - מהקובץ picture_selected.py"""
        try:
            # Load the overlay image once
            overlay_image = Image.open(overlay_image_path).convert("RGBA")
            # Resize the overlay image to the desired size
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
                    continue

                try:
                    # Open the original image
                    original_image = Image.open(source_file).convert("RGBA")

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

                    # Save the modified image with the new name
                    combined_image.save(new_file)
                except Exception as processing_error:
                    print(f"Error processing file {source_file}: {processing_error}")

        except Exception as general_error:
            print(f"An error occurred: {general_error}")
    
    # פונקציות עזר
    def save_settings(self, overlay_path, overlay_width, overlay_height, margin_top, margin_right, tab_type="all"):
        """שמירת הגדרות לקובץ JSON עם הפרדה בין טאבים"""
        # ניקוי placeholder אם קיים
        if overlay_path == "בחר תמונה לשכבת-על":
            overlay_path = ""
        
        # טעינת הגדרות קיימות
        current_settings = self.load_settings()
        
        # עדכון הגדרות לפי סוג הטאב
        if tab_type == "all":
            current_settings["all_files_overlay_path"] = overlay_path
        else:  # selected
            current_settings["selected_files_overlay_path"] = overlay_path
            
        # עדכון הגדרות משותפות
        current_settings["overlay_width"] = overlay_width
        current_settings["overlay_height"] = overlay_height
        current_settings["margin_top"] = margin_top
        current_settings["margin_right"] = margin_right
        
        try:
            # נסיון לשמור בתיקיית האפליקציה
            config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), CONFIG_FILE_NAME)
            with open(config_path, 'w', encoding='utf-8') as file_handler:
                json.dump(current_settings, file_handler, ensure_ascii=False, indent=2)
        except Exception as error_msg:
            try:
                # אם נכשל, ננסה בתיקיית המשתמש
                import tempfile
                config_path = os.path.join(tempfile.gettempdir(), CONFIG_FILE_NAME)
                with open(config_path, 'w', encoding='utf-8') as file_handler:
                    json.dump(current_settings, file_handler, ensure_ascii=False, indent=2)
            except Exception:
                print(f"לא ניתן לשמור הגדרות: {error_msg}")

    def load_settings(self):
        """טעינת הגדרות מקובץ JSON"""
        default_settings = {
            "all_files_overlay_path": "",  # נתיב נפרד לעיבוד כל הקבצים
            "selected_files_overlay_path": "",  # נתיב נפרד לקבצים נבחרים
            "overlay_width": 100,
            "overlay_height": 100,
            "margin_top": 10,
            "margin_right": 10,
            # תאימות לאחור - אם יש overlay_path ישן
            "overlay_path": ""
        }
        
        try:
            # נסיון לטעון מתיקיית האפליקציה
            config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), CONFIG_FILE_NAME)
            if not os.path.exists(config_path):
                # אם לא קיים, ננסה בתיקיית המשתמש
                import tempfile
                config_path = os.path.join(tempfile.gettempdir(), CONFIG_FILE_NAME)
            
            if os.path.exists(config_path):
                with open(config_path, 'r', encoding='utf-8') as file_handler:
                    settings = json.load(file_handler)
                    
                    # תאימות לאחור - אם יש overlay_path ישן, נעתיק אותו לשני הטאבים
                    if "overlay_path" in settings and settings["overlay_path"]:
                        if "all_files_overlay_path" not in settings:
                            settings["all_files_overlay_path"] = settings["overlay_path"]
                        if "selected_files_overlay_path" not in settings:
                            settings["selected_files_overlay_path"] = settings["overlay_path"]
                    
                    # וידוא שכל המפתחות קיימים
                    for key in default_settings:
                        if key not in settings:
                            settings[key] = default_settings[key]
                    return settings
        except Exception as error_msg:
            print(f"שגיאה בטעינת הגדרות: {error_msg}")
        
        return default_settings

    def show_progress_window(self, total_files, callback):
        """יצירת חלון progress bar יפה"""
        progress_window = Tk()
        progress_window.title("🔄 מעבד תמונות...")
        progress_window.geometry("500x200")
        progress_window.resizable(False, False)
        progress_window.configure(bg=self.colors['white'])
        
        # משתנים גלובליים
        is_cancelled = False
        
        # header
        header_frame = Frame(progress_window, bg=self.colors['secondary'], height=60)
        header_frame.pack(fill='x', padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        Label(header_frame, text="🔄 מעבד תמונות...", 
              font=("Arial", 16, "bold"), 
              fg=self.colors['white'], 
              bg=self.colors['secondary']).pack(expand=True)
        
        # תוכן
        content_frame = Frame(progress_window, bg=self.colors['white'])
        content_frame.pack(expand=True, fill='both', padx=30, pady=20)
        
        progress_var = StringVar(value="0/0")
        progress_label = Label(content_frame, textvariable=progress_var, 
                              font=("Arial", 12, "bold"), 
                              fg=self.colors['primary'], 
                              bg=self.colors['white'])
        progress_label.pack(pady=10)
        
        progress_bar = ttk.Progressbar(content_frame, length=400, mode='determinate')
        progress_bar.pack(pady=10)
        progress_bar['maximum'] = total_files
        
        status_label = Label(content_frame, text="מתחיל עיבוד...", 
                            font=("Arial", 11), 
                            fg=self.colors['dark'], 
                            bg=self.colors['white'])
        status_label.pack(pady=5)
        
        def cancel_callback():
            nonlocal is_cancelled
            is_cancelled = True
            progress_window.destroy()
        
        # כפתור ביטול
        cancel_button = Button(content_frame, text="❌ ביטול", 
                              command=cancel_callback,
                              font=("Arial", 11, "bold"),
                              bg=self.colors['danger'],
                              fg=self.colors['white'],
                              relief='flat',
                              padx=20,
                              pady=8)
        cancel_button.pack(pady=15)
        
        # הפעלת העיבוד באופן אסינכרוני בטוח
        def run_processing():
            try:
                callback(progress_var, progress_bar, status_label, lambda: is_cancelled)
            except Exception as error_msg:
                print(f"שגיאה בעיבוד: {error_msg}")
            finally:
                # עדכון UI במחזור הראשי
                progress_window.after(0, lambda: progress_window.destroy())
        
        # שימוש ב-after במקום threading
        progress_window.after(100, run_processing)
        
        # הפעלת החלון
        progress_window.mainloop()
        
        return is_cancelled
    
    def run(self):
        """הפעלת האפליקציה"""
        # הוספת handler לסגירת החלון
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def on_closing(self):
        """ניקוי bindings כשהחלון נסגר"""
        try:
            self.root.unbind_all("<MouseWheel>")
        except:
            pass
        self.root.destroy()

# הפעלת האפליקציה
if __name__ == "__main__":
    app = ImageProcessorApp()
    app.run()
