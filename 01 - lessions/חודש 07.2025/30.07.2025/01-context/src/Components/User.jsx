import { useContext } from "react"
import UserContext from "../Contexts/usercontext"

export function User(){
    const {user,setUser} = useContext(UserContext)


    return(
        <>
        <input type="text"
        placeholder="Enter UserName: "
        onChange={(e) => setUser(e.target.value)}
        />
        </>
    )
}