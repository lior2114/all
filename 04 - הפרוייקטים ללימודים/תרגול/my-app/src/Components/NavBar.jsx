import { useUser } from "../Contexts/userContext"
import { useNavigate, useLocation } from 'react-router-dom';


export function NavBar(){
    const navigate = useNavigate()
    const { user, logout } = useUser()
    
    const handleLogout = () => {
        logout()
        navigate("/")
    }
    
    return(
        <>
        <div>
        {user && user.user_id === 2 ? (
            <>
                <button 
                onClick={() => navigate("/")}
                >Home</button>

                <button 
                onClick={() => navigate("/About")}
                >About</button>
                
                <button 
                onClick={() => navigate("/vacations")}
                >Vacations</button>

                <button onClick={handleLogout}>Logout</button>
            </>
        ) : user && user.user_id === 1 ? (
            <>
                <button 
                onClick={() => navigate("/")}
                >Home</button>

                <button 
                onClick={() => navigate("/About")}
                >About</button>
                
                <button 
                onClick={() => navigate("/vacations")}
                >Vacations</button>

                <button 
                onClick={() => navigate("/createVacation")}
                >createVacation</button>

                <button onClick={handleLogout}>Logout</button>
            </>
        ) : (
            <>
                <button 
                onClick={() => navigate("/")}
                >Home</button>

                <button 
                onClick={() => navigate("/About")}
                >About</button>
                
                <button 
                onClick={() => navigate("/vacations")}
                >Vacations</button>

                <button onClick={() => navigate("/Login")}>Login</button>
            </>
        )}
        </div>
        </>
    )
}