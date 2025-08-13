import React, { createContext, useContext, useState, useEffect } from 'react';
import { login as loginAPI, register as registerAPI } from '../api/api';

// יצירת הקונטקסט
const UserContext = createContext();

// Hook לשימוש בקונטקסט
export const useUser = () => {
  const context = useContext(UserContext);
  if (!context) {
    throw new Error('useUser must be used within a UserProvider');
  }
  return context;
};

// Provider component
export const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // בדיקה אם יש משתמש בלוקל סטורג' בטעינה
  useEffect(() => {
    const savedUser = localStorage.getItem('user');
    if (savedUser) {
      try {
        const userData = JSON.parse(savedUser);
        setUser(userData);
      } catch (error) {
        localStorage.removeItem('user');
      }
    }
    setLoading(false);
  }, []);

  // פונקציה להתחברות
  const login = async (userData) => {
    try {
      setLoading(true);
      setError('');
      
      const result = await loginAPI(userData);
      
      // בדיקה אם השרת החזיר שגיאה
      if (result.Massages && result.Massages.includes("No users")) {
        throw new Error("אימייל או סיסמה שגויים");
      }
      
      // בדיקה אם יש user_id
      if (!result.user_id) {
        throw new Error("שגיאה בהתחברות - לא התקבל מזהה משתמש");
      }
      
      // שמירת פרטי המשתמש
      const userToSave = {
        user_email: userData.user_email,
        ...result
      };
      
      setUser(userToSave);
      localStorage.setItem('user', JSON.stringify(userToSave));
      
      return result;
    } catch (err) {
      setError(err.message || "שגיאה בהתחברות");
      throw err;
    } finally {
      setLoading(false);
    }
  };

  // פונקציה להרשמה
  const register = async (userData) => {
    try {
      setLoading(true);
      setError('');
      
      const result = await registerAPI(userData);
      
      // בדיקה אם השרת החזיר שגיאה
      if (result.Massages && result.Massages.includes("No users")) {
        throw new Error("שגיאה בהרשמה");
      }
      
      // בדיקה אם יש user_id
      if (!result.user_id) {
        throw new Error("שגיאה בהרשמה - לא התקבל מזהה משתמש");
      }
      
      // שמירת פרטי המשתמש
      const userToSave = {
        user_email: userData.user_email,
        ...result
      };
      
      setUser(userToSave);
      localStorage.setItem('user', JSON.stringify(userToSave));
      
      return result;
    } catch (err) {
      setError(err.message || "שגיאה בהרשמה");
      throw err;
    } finally {
      setLoading(false);
    }
  };

  // פונקציה להתנתקות
  const logout = () => {
    setUser(null);
    setError('');
    localStorage.removeItem('user');
  };

  // פונקציה לעדכון פרטי משתמש
  const updateUser = (newUserData) => {
    const updatedUser = { ...user, ...newUserData };
    setUser(updatedUser);
    localStorage.setItem('user', JSON.stringify(updatedUser));
  };

  // פונקציה לניקוי שגיאות
  const clearError = () => {
    setError('');
  };

  // ערך הקונטקסט
  const value = {
    user,
    loading,
    error,
    isAuthenticated: !!user,
    login,
    register,
    logout,
    updateUser,
    clearError
  };

  return (
    <UserContext.Provider value={value}>
      {children}
    </UserContext.Provider>
  );
};

export default UserContext;
