import { useNavigate } from "react-router-dom";

export default function Navbar() {
    const navigate = useNavigate();
    return (
        <nav style={{ display: 'flex', gap: 12, padding: 12, borderBottom: '1px solid #ddd' }}>
            <button type="button" onClick={() => navigate('/')}>Home</button>
            <button type="button" onClick={() => navigate('/register')}>Register</button>
            <button type="button" onClick={() => navigate('/login')}>Login</button>
        </nav>
    );
}


