import React, { createContext, useContext, useState, useEffect } from 'react';

export const TaskContext = createContext();

export const useTasks = () => {
    const context = useContext(TaskContext);
    if (!context) {
        throw new Error('useTasks must be used within a TasksProvider');
    }
    return context;
};

export const TasksProvider = ({ children }) => {
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [newTasks, setNewTasks] = useState([]);
    const [loading, setLoading] = useState(false);
    const [snackbarOpen, setSnackbarOpen] = useState(false);
    const [isInitialLoading, setIsInitialLoading] = useState(true);
  
    // הצגת loading spinner בטעינת האפליקציה
    useEffect(() => {
        // סימולציה של טעינה ראשונית
        const timer = setTimeout(() => {
            setIsInitialLoading(false);
            // הצגת הודעת ברוך הבא אחרי שהטעינה מסתיימת
            setTimeout(() => {
                setSnackbarOpen(true);
            }, 100);
        }, 500); // 0.5 שניות של loading

        return () => clearTimeout(timer);
    }, []);

    const handleCloseSnackbar = () => {
        setSnackbarOpen(false);
    };

    const btlhandle = () => {
        if (!title.trim() && !description.trim()) {
            return;
        }
        const newTask = {
            id: Date.now(), // יצירת ID ייחודי
            title: title,
            description: description,
            done: false
        };
        setNewTasks((prev) => [...prev, newTask]);
        setTitle("");
        setDescription("");
    };

    const toggleTaskStatus = (taskId) => {
        setNewTasks((prev) => prev.map(task => 
            task.id === taskId ? { ...task, done: !task.done } : task
        ));
    };

    const handleDelete = (taskId) => {
        setNewTasks((prev) => prev.filter((task) => task.id !== taskId));
    };

    const value = {
        title,
        setTitle,
        description,
        setDescription,
        newTasks,
        setNewTasks,
        loading,
        setLoading,
        snackbarOpen,
        handleCloseSnackbar,
        isInitialLoading,
        btlhandle,
        toggleTaskStatus,
        handleDelete
    };

    return (
        <TaskContext.Provider value={value}>
            {children}
        </TaskContext.Provider>
    );
};