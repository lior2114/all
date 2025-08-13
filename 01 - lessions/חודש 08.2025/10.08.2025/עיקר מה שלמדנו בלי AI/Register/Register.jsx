import { useState } from "react"
import { register } from "../../api/api"

// קומפוננטת Register - טופס הרשמה
export const Register = () => {
  // שלב 1 - יצירת state עבור הנתונים של הטופס
  // כאן אנחנו שומרים את הערכים של השדות שהמשתמש ממלא
  const [formData, setFormData] = useState({
    first_name:"",
    last_name: "",
    user_email: "",
    user_password: "",
  });

  // שלב 2 - פונקציה שמטפלת בשינוי של שדות הטופס
  // כל פעם שהמשתמש משנה ערך בשדה, הפונקציה הזו מתעדכנת
  const handleChange = (e) => {
    console.log(e.target.name); // מדפיס את שם השדה שהשתנה
    console.log(e.target.value); // מדפיס את הערך החדש
    setFormData({
      ...formData,
      [e.target.name]: e.target.value // מעדכן את הערך ב-state
    });
  };

  // שלב 3 - פונקציה שמטפלת בשליחת הטופס
  // כאשר המשתמש לוחץ על "Register", הפונקציה הזו מופעלת
  const handleRegister = async (e) => {
    e.preventDefault(); // מונע רענון של הדף
    try {
      // כאן אפשר להוסיף הודעות הצלחה/שגיאה אם רוצים
      const result = await register(formData); // שולח את הנתונים לשרת
      console.log("Registration result:", result); // מדפיס את התוצאה
    } catch (err) {
      console.error("Registration error:", err); // מדפיס שגיאה אם יש
      // אפשר להוסיף כאן סטייט להודעת שגיאה
    }
  };

  // שלב 4 - החזרת ה-JSX שמציג את הטופס למשתמש
  return (
    <div>
      <h1>Register</h1>
      <form onSubmit={handleRegister}>
        <input
          onChange={handleChange}
          name="first_name"
          type="text"
          placeholder="First Name"
        />
        <input
          onChange={handleChange}
          name="last_name"
          type="text"
          placeholder="Last Name"
        />
        <input
          onChange={handleChange}
          name="user_email"
          type="email"
          placeholder="Email"
        />
        <input
          onChange={handleChange}
          name="user_password"
          type="password"
          placeholder="Password"
        />
        <button type="submit">Register</button>
      </form>
    </div>
  );
};