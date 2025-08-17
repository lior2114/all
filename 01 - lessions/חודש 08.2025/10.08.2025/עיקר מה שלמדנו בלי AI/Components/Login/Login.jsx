import { useState } from "react"
import { login as loginapi } from "../../../api/api"
export const Login = () =>{
    const [formData, setFormData] = useState({
        user_email: "",
        user_password: ""
    })



const handleChange = (e) =>{
    setFormData({
        ...formData,
        [e.target.name]: e.target.value
    })
}

const handleLogin = async (e) =>{
    e.preventDefault()
    try{
        const result = await loginapi(formData)
        console.log("Login result", result)

    }
    catch(error){
        console.error("Login error", error)

    }
}


return (
    <form onSubmit={handleLogin}>
        <input type="email"
        name="user_email"
        placeholder="email"
        onChange={handleChange}
        />
        <input type="password"
        name="user_password"
        placeholder="password"
        onChange={handleChange}
        />
        <button type="submit">Click</button>
    </form>
    
)}