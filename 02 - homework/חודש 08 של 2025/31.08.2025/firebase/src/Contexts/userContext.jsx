import { Children, createContext, useContext, useState } from "react";
import {register as registerApi, login as loginApi, forgetpassword as forgetpasswordApi} from "../api/api"

export const userContext = createContext()

export const useUserContext = () =>{
    const context = useContext(userContext)
    if (!context){
        throw new Error("need to use context")
    }
    return context
}

export const UserProvider = ({children}) => {
    const [user, setUser] = useState("")
    const [loading, setLoading] = useState(false)
    const [authintication, setAuthintication] = useState(false)
    const [message, setMessage] = useState("")
    const [errormessage, setErrorMessage] = useState("")

    const register = async (email, password) => {
        try {
            setLoading(true)
            setMessage("")           // מנקה הודעות קודמות
            setErrorMessage("")      // מנקה הודעות שגיאה קודמות
            const userCredential = await registerApi(email, password)
            if (!userCredential) {
                setErrorMessage("Registration failed")
                setLoading(false)
                setAuthintication(false)
            }
            else {
                setUser(userCredential.user)
                setMessage("Registration successful")
                setLoading(false)
                setAuthintication(true)
            }
        }
        catch (err) {
            console.error(err)
            setErrorMessage("Registration failed: " + err.message)
            setLoading(false)
            setAuthintication(false)
        }
    }

    const login = async (email, password) => {
        try {
            setLoading(true)
            setMessage("")           // מנקה הודעות קודמות
            setErrorMessage("")      // מנקה הודעות שגיאה קודמות
            const userCredential = await loginApi(email, password)
            if (!userCredential) {
                setErrorMessage("no user found with that email address")
                setLoading(false)
                setAuthintication(false)
            }
            else {
                setUser(userCredential.user)
                setMessage("Login successfully")
                setLoading(false)
                setAuthintication(true)
            }
        }
        catch (err) {
            console.error(err)
            setErrorMessage("Login failed: " + err.message)
            setLoading(false)
            setAuthintication(false)
        }
    }

    const forgetpassword = async (email) =>{
        setLoading(true)
        setMessage("")           // מנקה הודעות קודמות
        setErrorMessage("")      // מנקה הודעות שגיאה קודמות
        try{
            const userCredential = await forgetpasswordApi(email)
            if (!userCredential){
                setErrorMessage("No such email in here")
                setLoading(false)
                setAuthintication(false)
            }else{
                setMessage("email sent")
                setLoading(false)
                setAuthintication(true)
            }
        }
        catch(err){
            console.error(err)
            setErrorMessage("some error: " + err.message)
            setLoading(false)
            setAuthintication(false)
        }
    }

    const value = {
        user,
        setUser,
        loading,
        errormessage,
        setErrorMessage,
        authintication,
        message,
        register,
        login,
        forgetpassword
    }

    return (
        <userContext.Provider value={value}>
            {children}
        </userContext.Provider>
    )
}