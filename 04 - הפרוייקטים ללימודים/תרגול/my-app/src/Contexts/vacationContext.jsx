import { createContext, useContext, useState, useEffect, Children } from "react";
import { getVacations as getVacationsAPI,
    updateVacation as updateVacationAPI, 
    deleteVacation as deleteVacationAPI,
    createVacation as createVacationAPI
} from "../api/api";


export const vacationContext = createContext()

export const useVacation = () => {
    const vacation = useContext(vacationContext)
    if (!vacation){
        throw new Error ("need to use vacation context")
    }
    else{
        return vacation
    }
    
}

export const VacationProvider = ({children}) => {
    const [vacationName, setVacationName] = useState("")
    const [vacationDescription, setVacationDescription] = useState("")
    const [loading, setLoading] = useState(false)
    const [authentication, setAuthentication] = useState(false)
    const [error, setError] = useState("")


// טעינה ראשונית
    // useEffect(() => {
    //     const fetchVacations = async () => {
    //         try {
    //             setError("")
    //             setLoading(true)
    //             const result = await getVacationsAPI()
    //             if (!result){
    //                 setError("No vacations has been added yet")
    //                 setAuthentication(false)
    //             } else {
    //                 setAuthentication(true)
    //                 return result
    //             }
    //             setLoading(false)
    //         } catch(err) {
    //             setError("failed to load vacations")
    //             setLoading(false)
    //         }
    //     }
    //     fetchVacations()
    // }, [])

    const getVacation = async() => {
        try {
            setLoading(true)
            setError("")
            const result = await getVacationsAPI()
            if (!result){
                setError("No vacations has been added yet")
                setAuthentication(false)
            } else {
                setAuthentication(true)
                return result
            }
            setLoading(false)
        } catch(err) {
            setError("failed to load vacations")
            setLoading(false)
        }
    }

    const updateVacation = async (id, userData) => {
        try {
            setLoading(true)
            setError("")
            const result = await updateVacationAPI(id, userData)
            if (!result) {
                setError("wrong Id or Wrong value")
                setAuthentication(false)
            } else {
                setAuthentication(true)
                return result
            }
        } catch(err) {
            setError("failed to do the action of update")
        } finally {
            setLoading(false)
        }
    }

    const deleteVacation = async (id) =>{
        try {
            setLoading(true)
            setError("")
            const result = await deleteVacationAPI(id)
            if (!result) {
                setError("wrong vacation Id")
                setAuthentication(false)
            } else {
                setAuthentication(true)
                return result
            }
        } catch(err) {
            setError("failed to do the action of Delete")
        } finally {
            setLoading(false)
        }
    }

    const createVacation = async (userData) =>{
        try {
            setLoading(true)
            setError("")
            const result = await createVacationAPI(userData)
            if (!result) {
                setError("wrong create Vacation")
                setAuthentication(false)
            } else {
                setAuthentication(true)
                return result
            }
        } catch(err) {
            setError("failed to create Vacation")
        } finally {
            setLoading(false)
        }
    }

    const value = {
        updateVacation,
        deleteVacation,
        createVacation,
        vacationName,
        setVacationName,
        vacationDescription,
        setVacationDescription,
        getVacation,
        loading,
        authentication,
        error,
        setError,
    }
    return (
        <vacationContext.Provider value={value}>
            {children}
        </vacationContext.Provider>
    )
}
