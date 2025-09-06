import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { onAuthChange, logoutUser } from "../api/firebase_api";
import styles from "./Navbar.module.css";

export default function Navbar() {
    const navigate = useNavigate();
    const [currentUser, setCurrentUser] = useState(null);

    useEffect(() => {
        const unsubscribe = onAuthChange((user) => setCurrentUser(user));
        return () => unsubscribe();
    }, []);

    const handleLogout = async () => {
        await logoutUser();
        navigate('/login');
    };

    return (
        <nav className={styles.container}>
            <button className={styles.button} type="button" onClick={() => navigate('/')}>Home</button>
            {!currentUser && ( 
                //הכוונה שזה החזיר null
                <>
                    <button className={styles.button} type="button" onClick={() => navigate('/register')}>Register</button>
                    <button className={styles.button} type="button" onClick={() => navigate('/login')}>Login</button>
                </>
            )}
            {/* אם יש משתמש  */}
            {currentUser && (
                <>
                    <span className={`${styles.spacer} ${styles.user}`}>{currentUser.email}</span>
                    <button className={styles.button} type="button" onClick={handleLogout}>Logout</button>
                </>
            )}
        </nav>
    );
}


