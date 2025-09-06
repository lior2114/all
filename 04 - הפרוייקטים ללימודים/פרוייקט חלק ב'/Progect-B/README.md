# פרויקט חופשות - Frontend

פרויקט React עם Material-UI לניהול חופשות.

## התקנה

1. התקן את ה-dependencies:
```bash
npm install @mui/material @emotion/react @emotion/styled @mui/icons-material react-router-dom
```

2. הפעל את השרת:
```bash
npm run dev
```

## תכונות

- **דף הרשמה**: עם validation מלא לכל השדות
- **בדיקת אימייל**: בדיקה בזמן אמת אם האימייל קיים במערכת
- **Validation**: 
  - שם פרטי ומשפחה - רק אותיות
  - אימייל - פורמט תקין
  - סיסמה - מינימום 4 תווים
- **UI יפה**: עם Material-UI
- **ניווט**: לדף חופשות אחרי הרשמה מוצלחת

## מבנה הפרויקט

- `src/Pages/Register.jsx` - דף הרשמה
- `src/Contexts/UserContexts.jsx` - ניהול מצב המשתמש
- `src/api/api.js` - קריאות API
- `src/App.jsx` - Routing ראשי

## API Endpoints

- `POST /users` - הרשמת משתמש חדש
- `GET /users/login` - התחברות
- `GET /users/check_email` - בדיקת זמינות אימייל
