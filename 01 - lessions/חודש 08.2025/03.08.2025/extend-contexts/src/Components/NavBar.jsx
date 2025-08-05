import { Link } from 'react-router-dom';
import { useUser } from '../Contexts/UserContext';
export function NavBar(){
    const{user,isAuthnticated, logout} = useUser();
    const handlelogout = () =>{
        logout();
    }
    return(
        <div>
        <Link to = "/"> Home</Link>
        <Link to = "Login">Login</Link>
        <Link to = "Register">Register</Link>
        </div>
    )
}