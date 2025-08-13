import React, { createContext, useContext, useState, useEffect } from 'react';
import { getVacations, getVacationImage } from '../api/api';

// יצירת הקונטקסט
const VacationsContext = createContext();

// Hook לשימוש בקונטקסט
export const useVacations = () => {
  const context = useContext(VacationsContext);
  if (!context) {
    throw new Error('useVacations must be used within a VacationsProvider');
  }
  return context;
};

// Provider component
export const VacationsProvider = ({ children }) => {
  const [vacations, setVacations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // טעינת חופשות
  const fetchVacations = async () => {
    try {
      setLoading(true);
      setError('');
      const vacationsData = await getVacations();
      setVacations(vacationsData);
    } catch (err) {
      setError('שגיאה בטעינת החופשות');
      console.error('Error fetching vacations:', err);
    } finally {
      setLoading(false);
    }
  };

  // פונקציות עזר
  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('he-IL', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  };

  const formatPrice = (price) => {
    return new Intl.NumberFormat('he-IL', {
      style: 'currency',
      currency: 'ILS'
    }).format(price);
  };

  const calculateDuration = (startDate, endDate) => {
    const start = new Date(startDate);
    const end = new Date(endDate);
    const diffTime = Math.abs(end - start);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    return diffDays;
  };

  // טעינת חופשות בטעינה הראשונית
  useEffect(() => {
    fetchVacations();
  }, []);

  // ערך הקונטקסט
  const value = {
    vacations,
    loading,
    error,
    fetchVacations,
    formatDate,
    formatPrice,
    calculateDuration,
    getVacationImage
  };

  return (
    <VacationsContext.Provider value={value}>
      {children}
    </VacationsContext.Provider>
  );
};

export default VacationsContext;
