import { createContext, useContext, useState, useEffect, Children } from "react";
import { addlike as addlikeAPI,
    unlike as unlikeAPI
} from "../api/api";


export const likesContext = createContext()

export const useLike = () => {
    const likes = useContext(likesContext)
    if (!likes){
        throw new Error ("need to use likes context")
    }
    else{
        return likes
    }
    
}

export const likesProvider = ({children}) => {
    const [loading, setLoading] = useState(false)
    const [authentication, setAuthentication] = useState(false)
    const [error, setError] = useState("")

    const addlike = async (user_id, vacation_id) => {
        try{
            setLoading(true)
            setError('')
            const response = await addlikeAPI(user_id, vacation_id)
            if (!response){
                setError("you need to sign in to add like")
                setAuthentication(false)
            }else{
                setAuthentication(true)
                return response
            }
            setLoading(false)
        }
        catch (err){
            console.error(err)
            throw err
        }
    }

    const unlike = async (user_id, vacation_id) => {
        try{
            setLoading(true)
            setError('')
            const response = await unlikeAPI(user_id, vacation_id)
            if (!response){
                setError("cant unlike")
                setAuthentication(false)
            }else{
                setAuthentication(true)
                return response
            }
            setLoading(false)
        }
        catch (err){
            console.error(err)
            throw err
        }
    }
    const value = {
        addlike,
        unlike,
        loading,
        authentication,
        error,
        setError,
    }
    return (
        <likesContext.Provider value={value}>
            {children}
        </likesContext.Provider>
    )
}
