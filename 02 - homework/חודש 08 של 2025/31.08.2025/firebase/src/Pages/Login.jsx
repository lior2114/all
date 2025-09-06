import { useState } from "react"
import { userContext, useUserContext } from "../Contexts/userContext"
import { useNavigate } from "react-router-dom"

export function Login(){

    const {login, user, message, errormessage, loading} = useUserContext()
    const navigate = useNavigate()
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    
    const handlelogin = async () => {
        try {
            const trylogin = await login(email, password)
            if (trylogin){
                navigate("/")
            }
        } catch (error) {
            console.error("Login error:", error)
        }
    }

    return(
        <div>
            <h1>Login</h1>

            <input
             type="text"
            name="email"
            placeholder="Enter your email"
            onChange={(e)=> setEmail(e.target.value)}
            />
            <input
             type="password"
            name="password"
            placeholder="Enter your password"
            onChange={(e)=> setPassword(e.target.value)}
            />

            <button onClick={handlelogin} disabled={loading}>
                {loading ? "Logging in..." : "Click to Login"}
            </button>
            
            {message && <p style={{color: 'green'}}>{message}</p>}
            {errormessage && <p style={{color: 'red'}}>{errormessage}</p>}

            <h2>{user}</h2>
        </div>
    )
} 