# Users API

מערכת ניהול משתמשים עם SQLite ו-Flask

## התקנה

1. התקן את התלויות:
```bash
pip install -r requirements.txt
```

2. הרץ את האפליקציה:
```bash
python app.py
```

השרת יפעל על `http://localhost:5000`

## מבנה הפרויקט

```
Data_base/
├── app.py                 # קובץ ראשי של האפליקציה
├── users.db              # בסיס הנתונים SQLite
├── requirements.txt      # תלויות Python
├── models/              # מודלים של בסיס הנתונים
│   ├── __init__.py
│   └── user_model.py
├── controllers/         # לוגיקה עסקית
│   ├── __init__.py
│   └── user_controller.py
└── routes/             # הגדרת נתיבים
    ├── __init__.py
    └── user_routes.py
```

## מבנה טבלת Users

| שדה | סוג | תיאור |
|-----|-----|-------|
| id | INTEGER | מפתח ראשי, מספר רץ אוטומטי |
| username | TEXT | שם משתמש ייחודי |
| email | TEXT | כתובת אימייל ייחודית |
| password | TEXT | סיסמה מוצפנת (SHA-256) |
| created_at | TIMESTAMP | תאריך ושעת יצירה |

## API Endpoints

### 1. יצירת משתמש חדש
```
POST /api/users/
Content-Type: application/json

{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "123456"
}
```

### 2. הצגת כל המשתמשים
```
GET /api/users/
```

### 3. הצגת משתמש לפי ID
```
GET /api/users/{user_id}
```

### 4. עדכון משתמש
```
PUT /api/users/{user_id}
Content-Type: application/json

{
    "username": "new_username",
    "email": "newemail@example.com",
    "password": "newpassword"
}
```

### 5. מחיקת משתמש
```
DELETE /api/users/{user_id}
```

## תכונות

- ✅ CORS מוגדר לכל המקורות
- ✅ הצפנת סיסמאות עם SHA-256
- ✅ ולידציה של פורמט אימייל
- ✅ בדיקת ייחודיות שם משתמש ואימייל
- ✅ טיפול בשגיאות
- ✅ תגובות JSON מובנות

## דוגמאות שימוש

### יצירת משתמש חדש
```bash
curl -X POST http://localhost:5000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "test_user",
    "email": "test@example.com",
    "password": "123456"
  }'
```

### קבלת כל המשתמשים
```bash
curl http://localhost:5000/api/users/
```

### עדכון משתמש
```bash
curl -X PUT http://localhost:5000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{
    "username": "updated_user"
  }'
```
