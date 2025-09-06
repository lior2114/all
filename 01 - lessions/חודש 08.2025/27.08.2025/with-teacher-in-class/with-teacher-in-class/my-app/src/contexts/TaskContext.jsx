import React, { createContext, useContext, useState, useEffect } from 'react';

//1. Create context
const TaskContext = createContext();

// Custom hook to use the context
export const useTaskContext = () => {
  const context = useContext(TaskContext);
  if (!context) {
    throw new Error('useTaskContext must be used within a TaskProvider');
  }
  return context;
};

// Provider component
export const TaskProvider = ({ children }) => {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Load tasks from localStorage on component mount
  useEffect(() => {
    const loadTasksFromStorage = () => {
      try {
        setLoading(true);
        const savedTasks = localStorage.getItem('tasks');
        if (savedTasks) {
          const parsedTasks = JSON.parse(savedTasks);
          setTasks(parsedTasks);
        }
      } catch (error) {
        setError('שגיאה בטעינת המשימות');
      } finally {
        setLoading(false);
      }
    };

    loadTasksFromStorage();
  }, []);

  // Initialize tasks from localStorage if empty
  useEffect(() => {
    if (!loading && tasks.length === 0) {
      const savedTasks = localStorage.getItem('tasks');
      if (savedTasks) {
        try {
          const parsedTasks = JSON.parse(savedTasks);
          if (parsedTasks.length > 0) {
            setTasks(parsedTasks);
          }
        } catch (error) {
          console.error('Error parsing saved tasks:', error);
        }
      }
    }
  }, [loading, tasks.length]);

  // Save tasks to localStorage whenever tasks change
  useEffect(() => {
    // Don't save during initial load
    if (!loading) {
      localStorage.setItem('tasks', JSON.stringify(tasks));
    }
  }, [tasks, loading]);

  // Action functions
  const addTask = (task) => {
    const newTask = {
      id: Date.now().toString(),
      title: task.title,
      description: task.description || '',
      isDone: false,
    };
    setTasks(prevTasks => [...prevTasks, newTask]);
    setError(null);
  };

  const updateTask = (taskId, updates) => {
    setTasks(prevTasks =>
      prevTasks.map(task =>
        task.id === taskId ? { ...task, ...updates } : task
      )
    );
    setError(null);
  };

  const deleteTask = (taskId) => {
    setTasks(prevTasks => prevTasks.filter(task => task.id !== taskId));
    setError(null);
  };

  const toggleComplete = (taskId) => {
    setTasks(prevTasks =>
      prevTasks.map(task =>
        task.id === taskId
          ? { ...task, isDone: !task.isDone }
          : task
      )
    );
    setError(null);
  };



  const value = {
    tasks,
    loading,
    error,
    addTask,
    updateTask,
    deleteTask,
    toggleComplete,
  };

  return (
    <TaskContext.Provider value={value}>
      {children}
    </TaskContext.Provider>
  );
};

export default TaskContext;
