import React, { createContext, useContext, useState, useEffect } from "react";

const UserContext = createContext();

export const useUser = () => {
    const context = useContext(UserContext)
    if (!context) {
        throw new Error("useUser must be used within a UserProvider")
    }
    return context;
}

export const UserProvider = ({ children }) => {
    const [user, setUser] = useState(null)
    const [isAuthenticated, setIsAuthenticated] = useState(false)
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const saveUser = localStorage.getItem("user")
        if (saveUser) {
            try {
                const userData = JSON.parse(saveUser)
                setUser(userData)
                setIsAuthenticated(true)
            }
            catch (error) {
                console.error("error: " + error)
                localStorage.removeItem("user")
            }
            setLoading(false);
        }
    }, [])


    const login = (userData) => {
        setUser(userData)
        setIsAuthenticated(true)
        localStorage.setItem("user", JSON.stringify(userData))
    }

    const logout = () => {
        setUser(null)
        setIsAuthenticated(false)
        localStorage.removeItem("user")
    }

    const updateUser = (newUser) => {
        const updateUser = { ...user, ...newUser}
        setUser(updateUser)
        localStorage.setItem("user", JSON.stringify(updateUser))//שם אותו ברשימה של הדיקשנרי
    }

    function getUserData() {
        const saveUser = localStorage.getItem("user")
        if (saveUser) {
            try {
                return JSON.parse(saveUser)//מחלץ אותו מהרשימה
            }
            catch (error) { console.error("error" + error) }
            return null
        }
    }

    const hasRole = (roleId) => {
        return user && user.role_id === roleId
    }

    const isAdmin = () => {
        return hasRole(1)
    }

    const value = {
        user,
        isAuthenticated,
        loading,
        login,
        logout,
        updateUser,
        getUserData,
        hasRole,
        isAdmin
    }

    return (
        <UserContext.Provider value={value}>
            {children}
        </UserContext.Provider>
    )
}