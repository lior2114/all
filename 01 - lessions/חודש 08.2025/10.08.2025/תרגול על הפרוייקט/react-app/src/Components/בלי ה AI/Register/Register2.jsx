import { useState } from "react"
import { register } from "../../../api/api"

export function Register(){
  const [message, setMessage] = useState("")
  const [error, setError] = useState("")
  
  const handleRegister = async () => {
    try {
      setMessage("")
      setError("")
        const result = await register({
          first_name: "Test",
          last_name: "User",
          user_email: "test@test.com",
          user_password: "test123"
        })
      setMessage("Registration successful!")
      console.log("Registration result:", result)
    } catch (err) {
      setError(err.message || "Registration failed")
      console.error("Registration error:", err)
    }
  }

  return(
    <div>
      <button onClick={handleRegister}>Register</button>
      { <p style={{color: 'green'}}>{message}</p>}
      {<p style={{color: 'red'}}>{error}</p>}
    </div>
  )
}