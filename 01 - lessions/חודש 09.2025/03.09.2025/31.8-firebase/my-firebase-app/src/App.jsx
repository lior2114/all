import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { useEffect } from 'react';
import './App.css';
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import AddMovies from "./pages/AddMovies";
import Movies from "./pages/Movies";
import { useUser } from './contexts/UserContext.jsx';

function App() {
  const { user, logout, loading } = useUser();


  const handleLogout = async () => {
    try {
      await logout();
      window.location.href = '/login';
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <Router
      future={{
        v7_startTransition: true,
        v7_relativeSplatPath: true
      }}
    >
      <div className="app">
        <nav className="navbar">
          <div className="nav-brand">
            <Link to="/">My Firebase App</Link>
          </div>
          <div className="nav-links">
            <Link to="/">Home</Link>
            {!loading && user && (
              <>
                <Link to="/movies">Movies</Link>
                <Link to="/add-movie">Add Movie</Link>
              </>
            )}
            {!loading && user ? (
              <>
                <button onClick={handleLogout}>Logout</button>
              </>
            ) : !loading ? (
              <>
                <Link to="/login">Login</Link>
                <Link to="/register">Register</Link>
              </>
            ) : (
              <span>Loading...</span>
            )}
          </div>
        </nav>
        
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/add-movie" element={<AddMovies />} />
            <Route path="/movies" element={<Movies />} />
          </Routes>
        </main>
      </div>
    </Router>
  )
}

export default App
