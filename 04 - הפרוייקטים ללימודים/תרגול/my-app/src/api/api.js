const API_URL = "http://localhost:5000";

export const login = async (userData) => {
    try {
        const response = await fetch(`${API_URL}/api/users/login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(userData)
        })
        if (!response.ok) {
            const errorData = await response.json()
            throw new Error(errorData.error || "Login fail")
        }
        return await response.json()
    }
    catch (error) {
        console.error("Login error", error);
        throw error;
    }
}

export const register = async (userData) => {
    try {
        const response = await fetch(`${API_URL}/api/users`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(userData)
        })
        if (!response.ok) {
            const errorData = await response.json()
            throw new Error(errorData.error || "register fail")
        }
        return await response.json()
    } catch (error) {
        console.error("Register error", error);
        throw error;
    }
}

export const getVacations = async () => {
    try {
        const response = await fetch(`${API_URL}/api/vacations`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        })
        if (!response.ok) {
            const errorData = await response.json()
            throw new Error(errorData.error || "Failed to fetch vacations")
        }
        return await response.json()
    }
    catch (error) {
        console.error("Get vacations error", error);
        throw error;
    }
}


export const createVacation = async (userData) => {
    try {
        // Add admin_user_id to the request
        const requestData = {
            ...userData,
            admin_user_id: 1 // Default admin ID - you might want to get this from context
        }
        
        const response = await fetch(`${API_URL}/api/vacations`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestData)
        })
        if (!response.ok) {
            const errorData = await response.json()
            throw new Error(errorData.error || "Failed to fetch vacations")
        }
        return await response.json()
    }
    catch (error) {
        console.error("create vacations error", error);
        throw error;
    }
}

export const updateVacation = async (id,userData) => {
    try {
        // Add admin_user_id to the request
        const requestData = {
            ...userData,
            admin_user_id: 1 // Default admin ID
        }
        
        const response = await fetch(`${API_URL}/api/vacations/update/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestData)
        })
        if (!response.ok) {
            const errorData = await response.json()
            throw new Error(errorData.error || "Failed to fetch vacations")
        }
        return await response.json()
    }
    catch (error) {
        console.error("update vacations error", error);
        throw error;
    }
}

export const deleteVacation = async (id) => {
    try {
        const response = await fetch(`${API_URL}/api/vacations/delete/${id}?admin_user_id=1`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json"
            }
        })
        if (!response.ok) {
            const errorData = await response.json()
            throw new Error(errorData.error || "Failed to fetch vacations")
        }
        return await response.json()
    }
    catch (error) {
        console.error("Delete vacations error", error);
        throw error;
    }
}


export const addlike = async (user_id, vacation_id) =>{
    try{
        const response = await fetch(`${API_URL}/api/likes`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ user_id, vacation_id })
        })
        if (!response.ok) {
            const errorData = await response.json()
            throw new Error(errorData.error || "Failed to add like")
        }
        return await response.json()
    }
    catch(err){
        console.error(err)
        throw err
    }
}

export const unlike = async (user_id, vacation_id) =>{
    try{
        const response = await fetch(`${API_URL}/api/likes`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ user_id, vacation_id })
        })
        if (!response.ok) {
            const errorData = await response.json()
            throw new Error(errorData.error || "Failed to unlike")
        }
        return await response.json()
    }
    catch(err){
        console.error(err)
        throw err
    }
}