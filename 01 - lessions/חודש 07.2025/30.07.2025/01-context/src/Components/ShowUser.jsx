import { useContext } from "react"
import UserContext from "../Contexts/usercontext"

export function ShowUser(){
    const {user,setUser} = useContext(UserContext)


    return(
        <>
            <div>{user}</div>
        </>
    )
}