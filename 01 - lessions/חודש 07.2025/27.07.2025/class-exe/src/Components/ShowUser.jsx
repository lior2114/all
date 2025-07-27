import { useState } from "react"
import { useContext } from "react"
import UserContext from "../Contexts/UserContext"

export function ShowUser(){
    const {user, setUser} = useContext(UserContext)
    const [message, setMessage] = useState("")

    function handleInput(e){
        setMessage(e.target.value)
    }

    function handleClick(){
        setUser(message)
    }

    return (
        <>
            <input 
                type="text"
                placeholder="enter username"
                value={message}
                onChange={handleInput}
            /> 
            <button onClick={handleClick}>click to Change</button>
        </>
    )
}