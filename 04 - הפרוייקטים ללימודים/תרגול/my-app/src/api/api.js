const API_URL = "http://localhost:5000";

export const login = async(userData) => {
    try{
        const response = await fetch(`${API_URL}/api/users/login`,{
            method: "POST",
            headers:{
                "Content-Type":  "application/json",
            },
            body: JSON.stringify(userData)
        })
        if (!response.ok){
            const errorData = await response.json()
            throw new Error(errorData.error || "Login fail")
        }
        return await response.json()
    }   
    catch (error){
            console.error("Login error", error);
            throw error;
        }
    }

export const register = async (userData) =>{
    try{
    const response = await fetch(`${API_URL}/api/users`,{
      method :"POST",
      headers:{
        "Content-Type" :"application/json"
      },
      body: JSON.stringify(userData)
    })
    if(!response.ok){
        const errorData = await response.json()
        throw new Error (errorData.error || "register fail")
    }
    return await response.json()
    }catch(error){
        throw new Error ("faild to register", error)
    }
}

