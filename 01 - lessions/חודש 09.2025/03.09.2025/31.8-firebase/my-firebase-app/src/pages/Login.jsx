import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useUser } from "../contexts/UserContext";

export default function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [errorMessage, setErrorMessage] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const navigate = useNavigate();
    const { login } = useUser();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setErrorMessage("");
        setIsLoading(true);
        
        try {
            await login(email, password);
            navigate("/");
        } catch (error) {
            console.error(error);
            
            // Handle specific Firebase auth errors
            switch (error.code) {
                case 'auth/user-not-found':
                    setErrorMessage("משתמש לא נמצא במערכת");
                    break;
                case 'auth/wrong-password':
                    setErrorMessage("סיסמא לא נכונה");
                    break;
                case 'auth/invalid-email':
                    setErrorMessage("כתובת אימייל לא תקינה");
                    break;
                case 'auth/too-many-requests':
                    setErrorMessage("יותר מדי ניסיונות התחברות. נסה שוב מאוחר יותר");
                    break;
                case 'auth/user-disabled':
                    setErrorMessage("המשתמש הושבת מהמערכת");
                    break;
                case 'auth/network-request-failed':
                    setErrorMessage("בעיית חיבור לאינטרנט");
                    break;
                default:
                    setErrorMessage("שגיאה בהתחברות. נסה שוב");
                    break;
            }
        } finally {
            setIsLoading(false);
        }
    }

    return (
        <div>
            <h1>התחברות</h1>
            <form onSubmit={handleSubmit}>
                <input 
                    type="email" 
                    placeholder="אימייל" 
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    disabled={isLoading}
                />
                <input 
                    type="password" 
                    placeholder="סיסמא" 
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    disabled={isLoading}
                />
                <button type="submit" disabled={isLoading}>
                    {isLoading ? "מתחבר..." : "התחבר"}
                </button>
                
                {/* Error Message Display */}
                {errorMessage && (
                    <div style={{
                        color: 'red',
                        marginTop: '10px',
                        padding: '10px',
                        backgroundColor: '#ffe6e6',
                        border: '1px solid #ff9999',
                        borderRadius: '5px',
                        textAlign: 'center'
                    }}>
                        {errorMessage}
                    </div>
                )}
            </form>
        </div>
    )
}
