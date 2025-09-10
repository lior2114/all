import { useState, useEffect } from "react"
import { useUser } from "../Contexts/userContext"
import { Link, useNavigate } from 'react-router-dom';

export function Login(){

    const {login, error, cleanError, setError} = useUser()
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        email: "",
        password: ""
    })

    // נקה שגיאות כשנכנסים לדף
    useEffect(() => {
        cleanError()
    }, [])    
    
    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        })
    }

    const handlelogin = async(e) =>{
        e.preventDefault()
        cleanError()
        
        // Validate form data
        if (!formData.email || !formData.password) {
            setError("Please fill in all fields");
            return;
        }
        
        try{
            await login(formData)
            navigate("/")
        }
        catch(error){
            // Error is handled by the context
        }
    }
    

    return(
        <>
         <h1>Login</h1>
         <form onSubmit={handlelogin}>
            <label>Email:</label>
            <input 
                type="email" 
                name="email"
                value={formData.email}
                onChange={handleChange}
                required
            />
            <label>Password:</label>
            <input 
                type="password" 
                name="password"
                value={formData.password}
                onChange={handleChange}
                required
            />
            <button type="submit">Login</button>
            {error && <p style={{color: 'red'}}>{error}</p>}

            <div>No user yet?
            please register 
            </div>
            <button onClick={()=>navigate("/Register")}>Register</button>
        </form>
        </>
    )
}