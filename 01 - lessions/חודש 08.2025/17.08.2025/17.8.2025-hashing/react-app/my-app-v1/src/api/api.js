const API_URL = "http://localhost:5003";
export const register = async (userData) => {
        console.log(userData)
        const response = await fetch(`${API_URL}/register`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(userData),
        });
        if(!response.ok){
            throw new Error("Failed to register");
        }
        let data = await response.json();
        return data;

}

export const login = async (userData) => {
    const response = await fetch(`${API_URL}/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(userData),
    });
    if(!response.ok){
        throw new Error("Failed to login");
    }
    let data = await response.json();
    return data;
}

