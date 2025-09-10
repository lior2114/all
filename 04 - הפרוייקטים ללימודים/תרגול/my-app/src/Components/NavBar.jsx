import { useUser } from "../Contexts/userContext"
import { useNavigate, useLocation } from 'react-router-dom';


export function NavBar(){
    const navigate = useNavigate()
    const { user, logout } = useUser()
    return(
        <>
        <div>
            <button 
            onClick={() => navigate("/")}
            >Home</button>

            <button 
            onClick={() => navigate("/About")}
            >About</button>

        {user? <button onClick={logout}>Logout</button> : <button onClick={() => navigate("/Login")}>Login</button>}    
        </div>
        </>
    )
}