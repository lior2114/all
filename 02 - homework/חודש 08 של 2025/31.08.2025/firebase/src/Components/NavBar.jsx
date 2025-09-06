import { Link } from "react-router-dom"

export function NavBar(){

    return (
        <div>
            <Link to="/">
                <button>Home</button>
            </Link>

            <Link to="/About">
                <button>About</button>
            </Link>

            <Link to="/Login">
                <button>Login</button>
            </Link>

            <Link to="/Register">
                <button>Register</button>
            </Link>
        </div>
    )
}