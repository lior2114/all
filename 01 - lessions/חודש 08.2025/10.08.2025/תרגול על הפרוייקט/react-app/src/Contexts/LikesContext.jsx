import React, { createContext, useContext, useState, useEffect } from 'react';
import { getLikes, addLike, removeLike } from '../api/api';
import { useUser } from './UserContext';

// יצירת הקונטקסט
const LikesContext = createContext();

// Hook לשימוש בקונטקסט
export const useLikes = () => {
  const context = useContext(LikesContext);
  if (!context) {
    throw new Error('useLikes must be used within a LikesProvider');
  }
  return context;
};

// Provider component
export const LikesProvider = ({ children }) => {
  const [likes, setLikes] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const { user } = useUser();

  // טעינת לייקים
  const fetchLikes = async () => {
    try {
      setLoading(true);
      setError('');
      const likesData = await getLikes();
      setLikes(likesData);
    } catch (err) {
      setError('שגיאה בטעינת הלייקים');
      console.error('Error fetching likes:', err);
    } finally {
      setLoading(false);
    }
  };

  // הוספת לייק
  const addLikeToVacation = async (vacationId) => {
    if (!user || !user.user_id) {
      throw new Error('אנא התחבר כדי לעשות לייק');
    }

    try {
      await addLike(user.user_id, vacationId);
      await fetchLikes(); // רענון הנתונים
    } catch (err) {
      throw err;
    }
  };

  // הסרת לייק
  const removeLikeFromVacation = async (vacationId) => {
    if (!user || !user.user_id) {
      throw new Error('אנא התחבר כדי להסיר לייק');
    }

    try {
      await removeLike(user.user_id, vacationId);
      await fetchLikes(); // רענון הנתונים
    } catch (err) {
      throw err;
    }
  };

  // טיפול בלייק/אנלייק
  const toggleLike = async (vacationId) => {
    if (!user || !user.user_id) {
      throw new Error('אנא התחבר כדי לעשות לייק');
    }

    const isLiked = isLikedByUser(vacationId);
    
    if (isLiked) {
      await removeLikeFromVacation(vacationId);
    } else {
      await addLikeToVacation(vacationId);
    }
  };

  // בדיקה אם המשתמש הנוכחי עשה לייק לחופשה
  const isLikedByUser = (vacationId) => {
    if (!user || !user.user_id) {
      return false;
    }
    return likes.some(like => like[0] === user.user_id && like[1] === vacationId);
  };

  // חישוב מספר הלייקים לכל חופשה
  const getLikesCount = (vacationId) => {
    return likes.filter(like => like[1] === vacationId).length;
  };

  // טעינת לייקים כשהמשתמש משתנה
  useEffect(() => {
    fetchLikes();
  }, [user]);

  // ערך הקונטקסט
  const value = {
    likes,
    loading,
    error,
    fetchLikes,
    addLikeToVacation,
    removeLikeFromVacation,
    toggleLike,
    isLikedByUser,
    getLikesCount
  };

  return (
    <LikesContext.Provider value={value}>
      {children}
    </LikesContext.Provider>
  );
};

export default LikesContext;
