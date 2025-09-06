import { useState } from "react";
import { registerUser } from "../api/firebase_api";
import styles from "./Register.module.css";
export default function Register() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await registerUser(email, password);
            setEmail("");
            setPassword("");
        } catch (error) {
            console.error(error);
        }
    }

    return (
        <div className={styles.container}>
            <h1>Register</h1>
            <form className={styles.form} onSubmit={handleSubmit}>
                <input className={styles.input} type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
                <input className={styles.input} type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
                <button className={styles.button} type="submit">Register</button>
            </form>
        </div>
    )
}