import { useState, useEffect } from "react"
import { useUser } from "../Contexts/userContext"
import { Link, useNavigate } from 'react-router-dom';

export function Register(){

    const {register, error, cleanError, setError} = useUser()
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        username: "",
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

    const handleRegister = async(e) =>{
        e.preventDefault()// עוצר את ה-refresh של הדף
        cleanError()
        // Validate form data
            if (!formData.email || !formData.password|| !formData.username) {
                setError("Please fill in all fields");
                return;
            }
        try{
            await register(formData)
            navigate("/")
        }
        catch(error){
            // Error is handled by the context
        }
    }
    

    return(
        <>
         <h1>Register</h1>
         <form onSubmit={handleRegister}>
            <label>UserName: </label>
            <input type="text"
            name = "username"
            value = {formData.username}
            onChange={handleChange}
            />
            <label>Email:</label>
            <input 
                type="email" 
                name="email"
                value={formData.email}
                onChange={handleChange}
            />
            <label>Password:</label>
            <input 
                type="password" 
                name="password"
                value={formData.password}
                onChange={handleChange}
            />
            <button type="submit">Register</button>
            {error && <p style={{color: 'red'}}>{error}</p>}
            <div>Already have User?
                Login <button onClick={()=> navigate("/Login")}>To Login</button>
            </div>
        </form>
        </>
    )
}