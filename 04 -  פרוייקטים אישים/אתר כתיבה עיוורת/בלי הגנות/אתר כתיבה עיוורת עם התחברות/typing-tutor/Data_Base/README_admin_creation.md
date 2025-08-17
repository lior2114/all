# יצירת משתמש אדמין - Admin User Creation

## תיאור / Description
סקריפט Python ליצירת משתמש אדמין במערכת לימוד הקלדה.
Python script for creating admin users in the typing tutor system.

## דרישות / Requirements
- Python 3.6+
- גישה לבסיס הנתונים / Database access
- המודולים הנדרשים מותקנים / Required modules installed

## שימוש / Usage

### הרצת הסקריפט / Running the Script
```bash
cd Data_Base
python create_admin.py
```

### שלבי היצירה / Creation Steps
1. **הזנת שם פרטי** - רק אותיות מותרות
   - Enter first name - letters only allowed

2. **הזנת שם משפחה** - רק אותיות מותרות
   - Enter last name - letters only allowed

3. **הזנת אימייל** - פורמט תקין נדרש
   - Enter email - valid format required

4. **הזנת סיסמה** - מינימום 4 תווים
   - Enter password - minimum 4 characters

5. **אימות סיסמה** - הזנה חוזרת לאימות
   - Confirm password - re-enter for verification

6. **אישור יצירה** - אישור סופי ליצירת המשתמש
   - Creation confirmation - final approval

## תכונות / Features

### ✅ בדיקות תקינות / Validation Checks
- **שם**: רק אותיות מותרות
  - Name: letters only allowed
- **אימייל**: פורמט תקין ובדיקת כפילות
  - Email: valid format and duplicate check
- **סיסמה**: מינימום 4 תווים ואימות
  - Password: minimum 4 characters and confirmation

### ✅ אבטחה / Security
- בדיקת כפילות אימייל
  - Email duplicate check
- אימות סיסמה כפול
  - Double password confirmation
- הצפנת סיסמה (אם נדרש)
  - Password hashing (if needed)

### ✅ תמיכה דו-לשונית / Bilingual Support
- הודעות בעברית ובאנגלית
  - Messages in Hebrew and English
- ממשק משתמש ידידותי
  - User-friendly interface

## פלט / Output
הסקריפט יציג:
The script will display:

```
==================================================
יצירת משתמש אדמין - Admin User Creation
==================================================

הזן את פרטי המשתמש האדמין:
Enter admin user details:

שם פרטי / First Name: [הזנה]
שם משפחה / Last Name: [הזנה]
אימייל / Email: [הזנה]
סיסמה / Password (מינימום 4 תווים): [הזנה]
אימות סיסמה / Confirm Password: [הזנה]

פרטי המשתמש האדמין:
Admin User Details:
------------------------------
שם פרטי / First Name: [שם]
שם משפחה / Last Name: [שם משפחה]
אימייל / Email: [אימייל]
תפקיד / Role: מנהל / Admin

האם ליצור את המשתמש האדמין? (y/n): [אישור]

✅ משתמש אדמין נוצר בהצלחה!
✅ Admin user created successfully!

פרטי המשתמש שנוצר:
Created User Details:
------------------------------
מזהה משתמש / User ID: [מספר]
שם מלא / Full Name: [שם מלא]
אימייל / Email: [אימייל]
תפקיד / Role: מנהל / Admin
תאריך יצירה / Created: [תאריך ושעה]

🎉 המשתמש האדמין מוכן לשימוש!
🎉 The admin user is ready to use!
```

## שגיאות נפוצות / Common Errors

### ❌ אימייל כבר קיים / Email Already Exists
```
❌ אימייל זה כבר קיים במערכת!
❌ This email already exists in the system!
```
**פתרון**: השתמש באימייל אחר או מחק את המשתמש הקיים
**Solution**: Use a different email or delete the existing user

### ❌ פורמט אימייל לא תקין / Invalid Email Format
```
❌ פורמט אימייל לא תקין!
❌ Invalid email format!
```
**פתרון**: הזן אימייל בפורמט תקין (example@domain.com)
**Solution**: Enter email in valid format (example@domain.com)

### ❌ סיסמה קצרה מדי / Password Too Short
```
❌ סיסמה חייבת להכיל לפחות 4 תווים!
❌ Password must contain at least 4 characters!
```
**פתרון**: הזן סיסמה עם לפחות 4 תווים
**Solution**: Enter password with at least 4 characters

### ❌ סיסמאות לא תואמות / Passwords Don't Match
```
❌ הסיסמאות אינן תואמות!
❌ Passwords do not match!
```
**פתרון**: הזן את אותה סיסמה בשני השדות
**Solution**: Enter the same password in both fields

## הערות חשובות / Important Notes

1. **הרשאות אדמין**: המשתמש שנוצר יהיה בעל הרשאות מנהל מלאות
   - Admin permissions: The created user will have full admin privileges

2. **בסיס נתונים**: הסקריפט יוצר את הטבלאות הנדרשות אם הן לא קיימות
   - Database: The script creates required tables if they don't exist

3. **גיבוי**: מומלץ לגבות את בסיס הנתונים לפני יצירת משתמשים חדשים
   - Backup: It's recommended to backup the database before creating new users

4. **אבטחה**: שמור על פרטי ההתחברות במקום בטוח
   - Security: Keep login credentials in a safe place

## תמיכה / Support
 caso של בעיות, בדוק:
In case of issues, check:

1. **התקנת Python**: ודא ש-Python 3.6+ מותקן
   - Python installation: Ensure Python 3.6+ is installed

2. **נתיבים**: ודא שהסקריפט רץ מתיקיית Data_Base
   - Paths: Ensure the script runs from the Data_Base directory

3. **הרשאות**: ודא שיש הרשאות קריאה/כתיבה לבסיס הנתונים
   - Permissions: Ensure read/write permissions for the database

4. **תלויות**: ודא שכל המודולים הנדרשים מותקנים
   - Dependencies: Ensure all required modules are installed
