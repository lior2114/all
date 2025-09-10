import { Children, createContext, useContext, useEffect, useState } from "react";
import { login as loginAPI} from "../api/api";
import { register as registerAPI} from "../api/api";

const userContexts = createContext()

export const useUser =  () =>{
    const context = useContext(userContexts)
    if (!context)
        throw new Error("useUser must be in use")
    return context
}

export const UserProvider = ({children}) => {
    const [user, setUser] = useState(null)
    const [loading , setLoading] = useState(true)
    const [error, setError] = useState("")

    useEffect(()=>{
        const saveuser = localStorage.getItem("user")
        if(saveuser){
            try{
                const userData = JSON.parse(saveuser)
                setUser(userData)
            }
            catch (error){
                localStorage.removeItem("user")
            }
        }
        setLoading(false)
    },[])

    const login = async (userData) =>{
        try {
            setLoading(true)
            setError("")
            const result = await loginAPI(userData)
            
            // Check if login was successful
            if (result.success && result.data) {
                const userToSave = {
                    email: userData.email,
                    ...result.data
                }
                setUser(userToSave)
                localStorage.setItem("user", JSON.stringify(userToSave))
                return result.data
            } else {
                throw new Error(result.error || "Login failed")
            }
        }
        catch (error){
            setError(error.message || "Error Login")
            throw error
        }
        finally{
            setLoading(false)
        }
    }

    const register = async (userData) => {
        try{
            setLoading(true)
            setError("")
            const result = await registerAPI(userData)

            // Check if registration was successful
            if (result.success && result.data) {
                const userToSave = {
                    email: userData.email,
                    ...result.data
                }
                setUser(userToSave)
                localStorage.setItem("user", JSON.stringify(userToSave))
                return result.data
            } else {
                throw new Error(result.error || "Registration failed")
            }
        }
        catch(error){
            setError(error.message || "Registration failed")
            throw error
        }
        finally{
            setLoading(false)
        }
    }

    const logout = () =>{
        setUser(null)
        setError("")
        localStorage.removeItem("user")
    }

    const cleanError = ()=>{
        setError("")
    }
    
    const values = {
        user,
        loading,
        error,
        setError, 
        login,
        register,
        logout,
        cleanError
    }

    return (
        <userContexts.Provider value={values}>
            {children}
        </userContexts.Provider>
    )
}

export default userContexts