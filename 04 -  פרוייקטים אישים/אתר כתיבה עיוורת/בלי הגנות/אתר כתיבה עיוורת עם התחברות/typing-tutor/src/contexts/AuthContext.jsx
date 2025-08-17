import React, { createContext, useContext, useState, useEffect } from 'react';
import AuthApi from '../api/authApi';

const AuthContext = createContext();

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // בדיקה אם המשתמש מחובר בעת טעינת האפליקציה
  useEffect(() => {
    const checkAuthStatus = () => {
      try {
        const savedUser = localStorage.getItem('user');
        if (savedUser) {
          const userData = JSON.parse(savedUser);
          setUser(userData);
        }
      } catch (error) {
        console.error('Error loading user from localStorage:', error);
        localStorage.removeItem('user');
      } finally {
        setLoading(false);
      }
    };

    checkAuthStatus();
  }, []);

  // התחברות
  const login = async (email, password) => {
    try {
      setError(null);
      setLoading(true);
      
      const userData = await AuthApi.login(email, password);
      
      // שמירת המשתמש ב-localStorage
      localStorage.setItem('user', JSON.stringify(userData));
      setUser(userData);
      
      return userData;
    } catch (error) {
      setError(error.message);
      throw error;
    } finally {
      setLoading(false);
    }
  };

  // הרשמה
  const register = async (firstName, lastName, email, password) => {
    try {
      setError(null);
      setLoading(true);
      
      const userData = await AuthApi.register(firstName, lastName, email, password);
      
      // התחברות אוטומטית לאחר הרשמה
      localStorage.setItem('user', JSON.stringify(userData));
      setUser(userData);
      
      return userData;
    } catch (error) {
      setError(error.message);
      throw error;
    } finally {
      setLoading(false);
    }
  };

  // התנתקות
  const logout = () => {
    localStorage.removeItem('user');
    setUser(null);
    setError(null);
  };

  // עדכון פרטי משתמש
  const updateProfile = async (userData) => {
    try {
      // לא מנקים שגיאה כאן כדי שהשגיאה תישאר אם יש בעיה
      setLoading(true);

      const result = await AuthApi.updateUserProfile(user.user_id, userData);
      
      // לא ממזגים שדות רגישים ישירות; טוענים מחדש את פרטי המשתמש מהשרת אם צריך
      const updatedUser = {
        ...user,
        first_name: userData.first_name ?? user.first_name,
        last_name: userData.last_name ?? user.last_name,
        user_email: userData.user_email ?? user.user_email,
      };
      localStorage.setItem('user', JSON.stringify(updatedUser));
      setUser(updatedUser);
      
      return updatedUser;
    } catch (error) {
      const errorMessage = error.message || 'שגיאה בעדכון הפרופיל';
      setError(errorMessage);
      // לא זורקים את השגיאה כדי שהיא תישאר במצב
      return null;
    } finally {
      setLoading(false);
    }
  };

  // עדכון תמונת פרופיל
  const updateProfileImage = async (imageUrl) => {
    try {
      setError(null);
      setLoading(true);
      
      await AuthApi.updateProfileImage(user.user_id, imageUrl);
      
      // עדכון המשתמש במצב
      const updatedUser = { ...user, profile_image: imageUrl };
      localStorage.setItem('user', JSON.stringify(updatedUser));
      setUser(updatedUser);
      
      return updatedUser;
    } catch (error) {
      setError(error.message);
      throw error;
    } finally {
      setLoading(false);
    }
  };

  // מחיקת תמונת פרופיל
  const removeProfileImage = async () => {
    try {
      setError(null);
      setLoading(true);
      
      await AuthApi.removeProfileImage(user.user_id);
      
      // עדכון המשתמש במצב
      const updatedUser = { ...user, profile_image: null };
      localStorage.setItem('user', JSON.stringify(updatedUser));
      setUser(updatedUser);
      
      return updatedUser;
    } catch (error) {
      setError(error.message);
      throw error;
    } finally {
      setLoading(false);
    }
  };

  // קבלת התקדמות משתמש
  const getUserProgress = async () => {
    try {
      setError(null);
      return await AuthApi.getUserProgress(user.user_id);
    } catch (error) {
      setError(error.message);
      throw error;
    }
  };

  // עדכון התקדמות משתמש
  const updateUserProgress = async (progressData) => {
    try {
      setError(null);
      return await AuthApi.updateUserProgress({
        ...progressData,
        user_id: user.user_id,
      });
    } catch (error) {
      setError(error.message);
      throw error;
    }
  };

  // בדיקה אם המשתמש הוא אדמין
  const isAdmin = () => {
    return user && user.role_name === 'admin';
  };

  // בדיקה אם המשתמש הוא מנחה
  const isModerator = () => {
    return user && (user.role_name === 'moderator' || user.role_name === 'admin');
  };

  // ניקוי שגיאות
  const clearError = () => {
    setError(null);
  };

  const value = {
    user,
    loading,
    error,
    login,
    register,
    logout,
    updateProfile,
    updateProfileImage,
    removeProfileImage,
    getUserProgress,
    updateUserProgress,
    isAdmin,
    isModerator,
    clearError,
    setError,
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};
