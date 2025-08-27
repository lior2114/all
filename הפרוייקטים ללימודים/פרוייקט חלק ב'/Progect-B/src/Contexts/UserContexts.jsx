import { Children, createContext, useContext, useEffect, useState } from "react";
import { login as loginAPI, register as registerAPI} from "../api/api";

const UserContexts = createContext();

export const UseUser = () => {
    const context = useContext(UserContexts)
    if (!context){
        throw new Error("Need to use Contexts")
    }
    return context
}

export const UserProvider = ({children}) => {
    const [user, setUser] = useState(() => {
        try{
            const raw = localStorage.getItem("user");
            return raw ? JSON.parse(raw) : null;
        } catch {
            return null;
        }
    })
    const [isAuthenticated, setIsAuthenticated] = useState(() => {
        try { return !!localStorage.getItem("user"); } catch { return false; }
    });
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState("")

    useEffect(()=>{
        try{
            const userData = localStorage.getItem("user")
            if (userData){
                const parsed = JSON.parse(userData)
                setUser(parsed)
                setIsAuthenticated(true)
            }
        }catch(err){
            console.error(err)
            localStorage.removeItem("user")
            setUser(null)
            setIsAuthenticated(false)
        }
    },[])

    const login = async (getdata) =>{
        setLoading(true)
        setError(null)
        try{
            const response = await loginAPI(getdata)
            console.log(response)
            localStorage.setItem("user", JSON.stringify(response))
            setUser(response)
            setIsAuthenticated(true)
            setLoading(false)
            return {success:true, user:response}
        }
        catch(error){
            const errorMessage = error.message || 'Login failed';
            setError(errorMessage);
            setLoading(false);
            throw error;
        }
    }

    const register = async (getdata) => {
        setLoading(true)
        setError(null)
        try{
            const response = await registerAPI(getdata)
            console.log(response)
            localStorage.setItem("user", JSON.stringify(response))
            setUser(response)
            setIsAuthenticated(true)
            setLoading(false)
            return {success:true, user:response}
        }
        catch(error){
            const errorMessage = error.message || 'Registration failed';
            setError(errorMessage);
            setLoading(false);
            throw error;
        }
    }   

    const logout = () => {
        localStorage.removeItem('user');
        setUser(null);
        setIsAuthenticated(false);
        setError(null);
    };

    const updatedUser = (getdata) => {
        const updatedUser = {...user, ...getdata}
        setUser(updatedUser)
        localStorage.setItem("user", JSON.stringify(updatedUser))
    }

    const clearError = () => {
        setError(null)
    }

    const value = {
        login,
        logout,
        register,
        updatedUser,
        clearError,
        user,
        error,
        isAuthenticated,
        loading
    }

    return(
        <UserContexts.Provider value = {value}>
            {children}
        </UserContexts.Provider>
    )
}