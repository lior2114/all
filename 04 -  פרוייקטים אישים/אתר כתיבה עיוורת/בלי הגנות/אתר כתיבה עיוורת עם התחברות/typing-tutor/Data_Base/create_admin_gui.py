#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ממשק גרפי ליצירת משתמש אדמין
GUI for creating admin user
"""

import sys
import os
import re
import hashlib
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# הוספת הנתיב למודולים
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Models.Users_Models import Users_Model as U

class AdminCreationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("יצירת משתמש אדמין - Admin User Creation")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # הגדרת סגנון
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # צבעים
        self.bg_color = "#f0f0f0"
        self.accent_color = "#4CAF50"
        self.error_color = "#f44336"
        self.warning_color = "#ff9800"
        
        self.root.configure(bg=self.bg_color)
        
        # יצירת הממשק
        self.create_widgets()
        
        # בדיקת משתמשים קיימים
        self.check_existing_users()
    
    def create_widgets(self):
        """יצירת אלמנטי הממשק"""
        
        # כותרת ראשית
        title_frame = tk.Frame(self.root, bg=self.bg_color)
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame,
            text="יצירת משתמש אדמין",
            font=("Arial", 24, "bold"),
            bg=self.bg_color,
            fg="#333333"
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Admin User Creation",
            font=("Arial", 16),
            bg=self.bg_color,
            fg="#666666"
        )
        subtitle_label.pack()
        
        # אזהרה אם יש משתמשים קיימים
        self.warning_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.warning_color,
            wraplength=550
        )
        self.warning_label.pack(pady=10)
        
        # מסגרת טופס
        form_frame = tk.Frame(self.root, bg=self.bg_color)
        form_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # שם פרטי
        tk.Label(
            form_frame,
            text="שם פרטי / First Name:",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            anchor="e"
        ).pack(anchor="w", pady=(0, 5))
        
        self.first_name_var = tk.StringVar()
        self.first_name_entry = ttk.Entry(
            form_frame,
            textvariable=self.first_name_var,
            font=("Arial", 12),
            width=40
        )
        self.first_name_entry.pack(fill="x", pady=(0, 15))
        
        # שם משפחה
        tk.Label(
            form_frame,
            text="שם משפחה / Last Name:",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            anchor="e"
        ).pack(anchor="w", pady=(0, 5))
        
        self.last_name_var = tk.StringVar()
        self.last_name_entry = ttk.Entry(
            form_frame,
            textvariable=self.last_name_var,
            font=("Arial", 12),
            width=40
        )
        self.last_name_entry.pack(fill="x", pady=(0, 15))
        
        # אימייל
        tk.Label(
            form_frame,
            text="אימייל / Email:",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            anchor="e"
        ).pack(anchor="w", pady=(0, 5))
        
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(
            form_frame,
            textvariable=self.email_var,
            font=("Arial", 12),
            width=40
        )
        self.email_entry.pack(fill="x", pady=(0, 15))
        
        # סיסמה
        tk.Label(
            form_frame,
            text="סיסמה / Password (מינימום 4 תווים):",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            anchor="e"
        ).pack(anchor="w", pady=(0, 5))
        
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(
            form_frame,
            textvariable=self.password_var,
            font=("Arial", 12),
            show="*",
            width=40
        )
        self.password_entry.pack(fill="x", pady=(0, 15))
        
        # אימות סיסמה
        tk.Label(
            form_frame,
            text="אימות סיסמה / Confirm Password:",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            anchor="e"
        ).pack(anchor="w", pady=(0, 5))
        
        self.confirm_password_var = tk.StringVar()
        self.confirm_password_entry = ttk.Entry(
            form_frame,
            textvariable=self.confirm_password_var,
            font=("Arial", 12),
            show="*",
            width=40
        )
        self.confirm_password_entry.pack(fill="x", pady=(0, 15))
        
        # תפקיד (תמיד אדמין)
        tk.Label(
            form_frame,
            text="תפקיד / Role:",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            anchor="e"
        ).pack(anchor="w", pady=(0, 5))
        
        self.role_var = tk.StringVar(value="מנהל / Admin")
        role_entry = ttk.Entry(
            form_frame,
            textvariable=self.role_var,
            font=("Arial", 12),
            state="readonly",
            width=40
        )
        role_entry.pack(fill="x", pady=(0, 15))
        
        # כפתורים
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=20)
        
        # כפתור יצירה
        self.create_button = tk.Button(
            button_frame,
            text="יצור משתמש אדמין / Create Admin User",
            font=("Arial", 14, "bold"),
            bg=self.accent_color,
            fg="white",
            command=self.create_admin_user,
            width=25,
            height=2,
            relief="flat",
            cursor="hand2"
        )
        self.create_button.pack(side="left", padx=10)
        
        # כפתור ניקוי
        clear_button = tk.Button(
            button_frame,
            text="נקה טופס / Clear Form",
            font=("Arial", 12),
            bg="#2196F3",
            fg="white",
            command=self.clear_form,
            width=15,
            height=2,
            relief="flat",
            cursor="hand2"
        )
        clear_button.pack(side="left", padx=10)
        
        # כפתור יציאה
        exit_button = tk.Button(
            button_frame,
            text="יציאה / Exit",
            font=("Arial", 12),
            bg="#f44336",
            fg="white",
            command=self.root.quit,
            width=10,
            height=2,
            relief="flat",
            cursor="hand2"
        )
        exit_button.pack(side="left", padx=10)
        
        # אזור הודעות
        self.message_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 11),
            bg=self.bg_color,
            fg="#333333",
            wraplength=550
        )
        self.message_label.pack(pady=10)
        
        # מידע על המשתמש שנוצר
        self.user_info_frame = tk.Frame(self.root, bg=self.bg_color)
        self.user_info_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        self.user_info_text = tk.Text(
            self.user_info_frame,
            height=8,
            font=("Arial", 10),
            bg="white",
            relief="solid",
            borderwidth=1,
            state="disabled"
        )
        self.user_info_text.pack(fill="both", expand=True)
    
    def check_existing_users(self):
        """בדיקה אם יש משתמשים קיימים במערכת"""
        try:
            all_users = U.get_all_users()
            if isinstance(all_users, list) and len(all_users) > 0:
                self.warning_label.config(
                    text="⚠️  אזהרה: כבר יש משתמשים במערכת! המשתמש החדש יהיה בעל הרשאות מנהל.\nWarning: Users already exist in the system! The new user will have admin privileges."
                )
        except Exception as e:
            self.warning_label.config(
                text=f"⚠️  שגיאה בבדיקת משתמשים קיימים: {str(e)}\nError checking existing users: {str(e)}"
            )
    
    def validate_email(self, email):
        """בדיקת תקינות כתובת אימייל"""
        pattern = r"[^@]+@[^@]+\.[^@]+"
        return re.match(pattern, email) is not None
    
    def validate_name(self, name):
        """בדיקת תקינות שם (רק אותיות)"""
        return name.isalpha() and len(name.strip()) > 0
    
    def validate_password(self, password):
        """בדיקת תקינות סיסמה"""
        return len(password.strip()) >= 4
    
    def show_message(self, message, message_type="info"):
        """הצגת הודעה למשתמש"""
        colors = {
            "info": "#333333",
            "success": "#4CAF50",
            "error": "#f44336",
            "warning": "#ff9800"
        }
        
        self.message_label.config(
            text=message,
            fg=colors.get(message_type, "#333333")
        )
        
        # ניקוי ההודעה אחרי 5 שניות
        self.root.after(5000, lambda: self.message_label.config(text=""))
    
    def clear_form(self):
        """ניקוי הטופס"""
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.email_var.set("")
        self.password_var.set("")
        self.confirm_password_var.set("")
        self.user_info_text.config(state="normal")
        self.user_info_text.delete(1.0, tk.END)
        self.user_info_text.config(state="disabled")
        self.show_message("הטופס נוקה / Form cleared", "info")
    
    def create_admin_user(self):
        """יצירת משתמש אדמין"""
        # קבלת הנתונים מהטופס
        first_name = self.first_name_var.get().strip()
        last_name = self.last_name_var.get().strip()
        user_email = self.email_var.get().strip()
        user_password = self.password_var.get().strip()
        confirm_password = self.confirm_password_var.get().strip()
        
        # בדיקות תקינות
        if not first_name:
            self.show_message("❌ שם פרטי הוא שדה חובה!\n❌ First name is required!", "error")
            self.first_name_entry.focus()
            return
        
        if not self.validate_name(first_name):
            self.show_message("❌ שם פרטי חייב להכיל רק אותיות!\n❌ First name must contain only letters!", "error")
            self.first_name_entry.focus()
            return
        
        if not last_name:
            self.show_message("❌ שם משפחה הוא שדה חובה!\n❌ Last name is required!", "error")
            self.last_name_entry.focus()
            return
        
        if not self.validate_name(last_name):
            self.show_message("❌ שם משפחה חייב להכיל רק אותיות!\n❌ Last name must contain only letters!", "error")
            self.last_name_entry.focus()
            return
        
        if not user_email:
            self.show_message("❌ אימייל הוא שדה חובה!\n❌ Email is required!", "error")
            self.email_entry.focus()
            return
        
        if not self.validate_email(user_email):
            self.show_message("❌ פורמט אימייל לא תקין!\n❌ Invalid email format!", "error")
            self.email_entry.focus()
            return
        
        if not user_password:
            self.show_message("❌ סיסמה היא שדה חובה!\n❌ Password is required!", "error")
            self.password_entry.focus()
            return
        
        if not self.validate_password(user_password):
            self.show_message("❌ סיסמה חייבת להכיל לפחות 4 תווים!\n❌ Password must contain at least 4 characters!", "error")
            self.password_entry.focus()
            return
        
        if user_password != confirm_password:
            self.show_message("❌ הסיסמאות אינן תואמות!\n❌ Passwords do not match!", "error")
            self.confirm_password_entry.focus()
            return
        
        # בדיקה אם האימייל כבר קיים
        try:
            if U.if_mail_exists(user_email):
                self.show_message("❌ אימייל זה כבר קיים במערכת!\n❌ This email already exists in the system!", "error")
                self.email_entry.focus()
                return
        except Exception as e:
            self.show_message(f"❌ שגיאה בבדיקת אימייל: {str(e)}\n❌ Error checking email: {str(e)}", "error")
            return
        
        # אישור יצירה
        confirm = messagebox.askyesno(
            "אישור יצירה / Creation Confirmation",
            f"האם ליצור את המשתמש האדמין?\n\n"
            f"שם: {first_name} {last_name}\n"
            f"אימייל: {user_email}\n"
            f"תפקיד: מנהל / Admin\n\n"
            f"Create admin user?\n\n"
            f"Name: {first_name} {last_name}\n"
            f"Email: {user_email}\n"
            f"Role: Admin"
        )
        
        if not confirm:
            self.show_message("יצירת המשתמש בוטלה / User creation cancelled", "info")
            return
        
        # יצירת המשתמש
        try:
            self.create_button.config(state="disabled", text="יוצר... / Creating...")
            self.root.update()
            
            # יצירת המשתמש
            result = U.create_user(
                first_name=first_name,
                last_name=last_name,
                user_email=user_email,
                user_password=user_password
            )
            
            if "user_id" in result:
                # עדכון התפקיד לאדמין
                U.update_user_by_id(result["user_id"], {"role_id": 1})
                result["role_id"] = 1
                
                # הצגת פרטי המשתמש שנוצר
                self.display_user_info(result)
                
                self.show_message(
                    "✅ משתמש אדמין נוצר בהצלחה!\n✅ Admin user created successfully!",
                    "success"
                )
                
                # ניקוי הטופס
                self.clear_form()
                
            else:
                self.show_message(
                    f"❌ שגיאה ביצירת המשתמש!\n❌ Error creating user!\nפרטים / Details: {result}",
                    "error"
                )
                
        except Exception as e:
            self.show_message(
                f"❌ שגיאה ביצירת המשתמש!\n❌ Error creating user!\nפרטי השגיאה / Error details: {str(e)}",
                "error"
            )
        
        finally:
            self.create_button.config(state="normal", text="יצור משתמש אדמין / Create Admin User")
    
    def display_user_info(self, user_data):
        """הצגת פרטי המשתמש שנוצר"""
        self.user_info_text.config(state="normal")
        self.user_info_text.delete(1.0, tk.END)
        
        info_text = f"""
פרטי המשתמש שנוצר / Created User Details:
{'='*50}

מזהה משתמש / User ID: {user_data['user_id']}
שם מלא / Full Name: {user_data['first_name']} {user_data['last_name']}
אימייל / Email: {user_data['user_email']}
תפקיד / Role: מנהל / Admin
תאריך יצירה / Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

🎉 המשתמש האדמין מוכן לשימוש!
🎉 The admin user is ready to use!

שים לב / Note:
- שמור את פרטי ההתחברות במקום בטוח
- Keep login credentials in a safe place
- המשתמש יכול להתחבר למערכת כעת
- User can now login to the system
"""
        
        self.user_info_text.insert(1.0, info_text)
        self.user_info_text.config(state="disabled")

def main():
    """פונקציה ראשית"""
    try:
        # יצירת חלון ראשי
        root = tk.Tk()
        
        # הגדרת אייקון (אם קיים)
        try:
            root.iconbitmap("icon.ico")
        except:
            pass
        
        # יצירת הממשק
        app = AdminCreationGUI(root)
        
        # הרצת הממשק
        root.mainloop()
        
    except Exception as e:
        # אם יש שגיאה ביצירת הממשק הגרפי, נחזור לממשק טקסט
        print("❌ שגיאה ביצירת הממשק הגרפי!")
        print("❌ Error creating GUI!")
        print(f"פרטי השגיאה / Error details: {str(e)}")
        print()
        print("מנסה להריץ את הממשק הטקסט...")
        print("Trying to run text interface...")
        
        # הרצת הממשק הטקסט
        try:
            from create_admin import main as text_main
            text_main()
        except Exception as e2:
            print(f"❌ שגיאה גם בממשק הטקסט: {str(e2)}")
            print(f"❌ Error in text interface too: {str(e2)}")

if __name__ == "__main__":
    main()
