import { useState } from "react"
import { UserProvider, useUserContext } from "../Contexts/userContext"

export function Register() {

    const { register, errormessage, message } = useUserContext()
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    const handlergister = async () => {
        try {
            const tryregister = register(email, password)
        }
        catch (err) {
            console.error("Register error" + err)
        }
    }

    return (
        <div>
            <h1>Register</h1>
            <input
                type="text"
                name="email"
                placeholder="Enter your email"
                onChange={(e) => setEmail(e.target.value)}
            />
            <input
                type="password"
                name="password"
                placeholder="Enter your password"
                onChange={(e) => setPassword(e.target.value)}
            />
            <button onClick={handlergister}>click to register</button>
            {message && <p style={{color: 'green'}}>{message}</p>}
            {errormessage && <p style={{color: 'red'}}>{errormessage}</p>}
       </div>
    )
}