import { useState } from "react";
import { loginUser } from "../api/firebase_api";
import { useNavigate } from "react-router-dom";
import styles from "./Login.module.css";

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
        <div className={styles.container}>
            <h1>Login</h1>
            <form className={styles.form} onSubmit={handleSubmit}>
                <input className={styles.input} type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
                <input className={styles.input} type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
                <button className={styles.button} type="submit">Login</button>
            </form>
            {error && <p className={styles.error}>{error}</p>}
        </div>
    );
}


