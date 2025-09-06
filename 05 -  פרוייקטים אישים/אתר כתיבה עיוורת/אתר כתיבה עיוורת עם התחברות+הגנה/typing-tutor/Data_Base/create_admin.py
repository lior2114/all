#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
סקריפט ליצירת משתמש אדמין
Script for creating admin user
"""

import sys
import os
import re
import hashlib
from datetime import datetime

# הוספת הנתיב למודולים
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Models.Users_Models import Users_Model as U

def validate_email(email):
    """בדיקת תקינות כתובת אימייל"""
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(pattern, email) is not None

def validate_name(name):
    """בדיקת תקינות שם (רק אותיות)"""
    return name.isalpha() and len(name.strip()) > 0

def validate_password(password):
    """בדיקת תקינות סיסמה"""
    return len(password.strip()) >= 4

def hash_password(password):
    """הצפנת סיסמה"""
    return hashlib.sha256(password.encode()).hexdigest()

def create_admin_user():
    """יצירת משתמש אדמין"""
    print("=" * 50)
    print("יצירת משתמש אדמין - Admin User Creation")
    print("=" * 50)
    print()
    
    # בדיקה אם כבר יש משתמשים במערכת
    all_users = U.get_all_users()
    if isinstance(all_users, list) and len(all_users) > 0:
        print("⚠️  אזהרה: כבר יש משתמשים במערכת!")
        print("אם תיצור משתמש אדמין נוסף, הוא יהיה בעל הרשאות מנהל.")
        print()
    
    # הזנת פרטי המשתמש
    print("הזן את פרטי המשתמש האדמין:")
    print("Enter admin user details:")
    print()
    
    # שם פרטי
    while True:
        first_name = input("שם פרטי / First Name: ").strip()
        if validate_name(first_name):
            break
        print("❌ שם פרטי חייב להכיל רק אותיות!")
        print("❌ First name must contain only letters!")
    
    # שם משפחה
    while True:
        last_name = input("שם משפחה / Last Name: ").strip()
        if validate_name(last_name):
            break
        print("❌ שם משפחה חייב להכיל רק אותיות!")
        print("❌ Last name must contain only letters!")
    
    # אימייל
    while True:
        user_email = input("אימייל / Email: ").strip()
        if validate_email(user_email):
            if not U.if_mail_exists(user_email):
                break
            else:
                print("❌ אימייל זה כבר קיים במערכת!")
                print("❌ This email already exists in the system!")
        else:
            print("❌ פורמט אימייל לא תקין!")
            print("❌ Invalid email format!")
    
    # סיסמה
    while True:
        user_password = input("סיסמה / Password (מינימום 4 תווים): ").strip()
        if validate_password(user_password):
            # אימות סיסמה
            confirm_password = input("אימות סיסמה / Confirm Password: ").strip()
            if user_password == confirm_password:
                break
            else:
                print("❌ הסיסמאות אינן תואמות!")
                print("❌ Passwords do not match!")
        else:
            print("❌ סיסמה חייבת להכיל לפחות 4 תווים!")
            print("❌ Password must contain at least 4 characters!")
    
    print()
    print("פרטי המשתמש האדמין:")
    print("Admin User Details:")
    print("-" * 30)
    print(f"שם פרטי / First Name: {first_name}")
    print(f"שם משפחה / Last Name: {last_name}")
    print(f"אימייל / Email: {user_email}")
    print(f"תפקיד / Role: מנהל / Admin")
    print()
    
    # אישור יצירה
    confirm = input("האם ליצור את המשתמש האדמין? (y/n): ").strip().lower()
    if confirm not in ['y', 'yes', 'כן', 'י']:
        print("❌ יצירת המשתמש בוטלה.")
        print("❌ User creation cancelled.")
        return
    
    try:
        # יצירת המשתמש
        print("🔄 יוצר משתמש...")
        print("🔄 Creating user...")
        
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
            
            print()
            print("✅ משתמש אדמין נוצר בהצלחה!")
            print("✅ Admin user created successfully!")
            print()
            print("פרטי המשתמש שנוצר:")
            print("Created User Details:")
            print("-" * 30)
            print(f"מזהה משתמש / User ID: {result['user_id']}")
            print(f"שם מלא / Full Name: {result['first_name']} {result['last_name']}")
            print(f"אימייל / Email: {result['user_email']}")
            print(f"תפקיד / Role: מנהל / Admin")
            print(f"תאריך יצירה / Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print()
            print("🎉 המשתמש האדמין מוכן לשימוש!")
            print("🎉 The admin user is ready to use!")
            
        else:
            print("❌ שגיאה ביצירת המשתמש!")
            print("❌ Error creating user!")
            print(f"פרטים / Details: {result}")
            
    except Exception as e:
        print("❌ שגיאה ביצירת המשתמש!")
        print("❌ Error creating user!")
        print(f"פרטי השגיאה / Error details: {str(e)}")

def main():
    """פונקציה ראשית"""
    try:
        # בדיקה שהטבלאות קיימות
        U.create_table()
        
        # יצירת משתמש אדמין
        create_admin_user()
        
    except Exception as e:
        print("❌ שגיאה כללית!")
        print("❌ General error!")
        print(f"פרטי השגיאה / Error details: {str(e)}")
        print()
        print("ודא שהנתיב לבסיס הנתונים נכון ושהמערכת מוכנה.")
        print("Make sure the database path is correct and the system is ready.")

if __name__ == "__main__":
    main()
