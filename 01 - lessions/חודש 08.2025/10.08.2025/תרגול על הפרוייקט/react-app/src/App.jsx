import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { CacheProvider } from '@emotion/react';
import createCache from '@emotion/cache';
import { prefixer } from 'stylis';
import rtlPlugin from 'stylis-plugin-rtl';
import { UserProvider } from './Contexts/UserContext';
import { VacationsProvider } from './Contexts/VacationsContext';
import { LikesProvider } from './Contexts/LikesContext';
import NavBar from './Components/NavBar/NavBar';
import Home from './Pages/Home';
import About from './Pages/About';
import Vacations from './Pages/Vacations';
import Login from './Pages/Login';
import Register from './Pages/Register';
import Profile from './Pages/Profile';
import Statistics from './Pages/Statistics';
import Admin from './Pages/Admin';
import './App.css';

// יצירת cache ל-RTL
const cacheRtl = createCache({
  key: 'muirtl',
  stylisPlugins: [prefixer, rtlPlugin],
});

// יצירת theme עם תמיכה ב-RTL
const theme = createTheme({
  direction: 'rtl',
  typography: {
    fontFamily: 'Rubik, Arial, sans-serif',
  },
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

function App() {
  return (
    <CacheProvider value={cacheRtl}>
      <ThemeProvider theme={theme}>
        <UserProvider>
          <VacationsProvider>
            <LikesProvider>
              <Router>
                <div className="App">
                  <NavBar />
                  <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/about" element={<About />} />
                    <Route path="/vacations" element={<Vacations />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/register" element={<Register />} />
                    <Route path="/profile" element={<Profile />} />
                    <Route path="/statistics" element={<Statistics />} />
                    <Route path="/admin" element={<Admin />} />
                  </Routes>
                </div>
              </Router>
            </LikesProvider>
          </VacationsProvider>
        </UserProvider>
      </ThemeProvider>
    </CacheProvider>
  );
}

export default App;
