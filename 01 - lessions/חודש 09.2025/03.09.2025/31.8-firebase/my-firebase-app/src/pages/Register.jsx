import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useUser } from "../contexts/UserContext";

export default function Register() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [errorMessage, setErrorMessage] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const navigate = useNavigate();
    const { register } = useUser();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setErrorMessage("");
        setIsLoading(true);
        
        try {
            await register(email, password);
            navigate("/");
        } catch (error) {
            console.error(error);
            
            // Handle specific Firebase auth errors
            switch (error.code) {
                case 'auth/email-already-in-use':
                    setErrorMessage("כתובת האימייל כבר קיימת במערכת");
                    break;
                case 'auth/invalid-email':
                    setErrorMessage("כתובת אימייל לא תקינה");
                    break;
                case 'auth/weak-password':
                    setErrorMessage("הסיסמא חייבת להכיל לפחות 6 תווים");
                    break;
                case 'auth/operation-not-allowed':
                    setErrorMessage("הרשמה לא מאושרת במערכת");
                    break;
                case 'auth/network-request-failed':
                    setErrorMessage("בעיית חיבור לאינטרנט");
                    break;
                default:
                    setErrorMessage("שגיאה בהרשמה. נסה שוב");
                    break;
            }
        } finally {
            setIsLoading(false);
        }
    }

    return (
        <div>
            <h1>הרשמה</h1>
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
                    {isLoading ? "נרשם..." : "הירשם"}
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


