import { useState } from "react";
import { loginUser } from "../api/firebase_api";
import { useNavigate } from "react-router-dom";

export default function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const navigate = useNavigate()
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        setError("");
        try {
            await loginUser(email, password);
            setEmail("");
            setPassword("");
            setError("login succefull")
            navigate("/")
        } catch (err) {
            setError(err?.message || "Login failed");
        }
    };

    return (
        <div>
            <h1>Login</h1>
            <form onSubmit={handleSubmit}>
                <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
                <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
                <button type="submit">Login</button>
            </form>
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
}


