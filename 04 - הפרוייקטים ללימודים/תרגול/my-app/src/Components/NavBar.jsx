import { useUser } from "../Contexts/userContext"
import { useNavigate, useLocation } from 'react-router-dom';

export function NavBar(){
    const navigate = useNavigate()
    return(
        <>
        <div>
            <button 
            onClick={() => navigate("/")}
            >Home</button>

            <button 
            onClick={() => navigate("/About")}
            >About</button>
            <button 
            onClick={() => navigate("/Login")}
            >Login</button>
            
        </div>
        </>
    )
}