import React, { createContext, useContext, useState, useEffect } from 'react';
import { login as loginAPI, register as registerAPI } from '../api/api';

// Create context
const UserContext = createContext();

// Custom hook to use the context
export const useUser = () => {
  const context = useContext(UserContext);
  if (!context) {
    throw new Error('useUser must be used within a UserProvider');
  }
  return context;
};

// Provider component
export const UserProvider = ({ children }) => {
  // State management with regular useState
  const [user, setUser] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Check if user is already logged in on app start
  useEffect(() => {
    const checkAuthStatus = () => {
      const userData = localStorage.getItem('user');
      
      if (userData) {
        try {
          const user = JSON.parse(userData);
          setUser(user);
          setIsAuthenticated(true);
        } catch (error) {
          console.error('Error parsing user data:', error);
          localStorage.removeItem('user');
        }
      }
    };

    checkAuthStatus();
  }, []);

  // Login function
  const login = async (credentials) => {
    setLoading(true);
    setError(null);
    
    try {
      // Call the real login API
      const response = await loginAPI(credentials);
      console.log('Login response:', response);
      
      // Store user data (without token)
      localStorage.setItem('user', JSON.stringify(response));
      
      // Update state
      setUser(response);
      setIsAuthenticated(true);
      setLoading(false);
      
      return { success: true, user: response };
      
    } catch (error) {
      const errorMessage = error.message || 'Login failed';
      setError(errorMessage);
      setLoading(false);
      throw error;
    }
  }; 

  // Register function
  const register = async (userData) => {
    setLoading(true);
    setError(null);
    
    try {
      // Call the real register API
      const response = await registerAPI(userData);
      console.log('Register response:', response);
      
      setLoading(false);
      return { success: true, data: response };
      
    } catch (error) {
      const errorMessage = error.message || 'Registration failed';
      setError(errorMessage);
      setLoading(false);
      throw error;
    }
  };

  // Logout function
  const logout = () => {
    localStorage.removeItem('user');
    setUser(null);
    setIsAuthenticated(false);
    setError(null);
  };

  // Update user function
  const updateUser = (updates) => {
    const updatedUser = { ...user, ...updates };
    setUser(updatedUser);
    
    // Update localStorage
    localStorage.setItem('user', JSON.stringify(updatedUser));
  };

  // Clear error function
  const clearError = () => {
    setError(null);
  };

  // Context value
  const value = {
    // State
    user,
    isAuthenticated,
    loading,
    error,
    
    // Functions
    login,
    logout,
    register,
    updateUser,
    clearError,
    
    // Computed values
    isAdmin: user?.role === 'admin',
    isUser: user?.role === 'user',
    userFullName: user ? `${user.first_name || ''} ${user.last_name || ''}`.trim() : '',
    userInitials: user && user.first_name && user.last_name ? 
      `${user.first_name[0]}${user.last_name[0]}` : ''
  };

  return (
    <UserContext.Provider value={value}>
      {children}
    </UserContext.Provider>
  );
};

export default UserContext;
