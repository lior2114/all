import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter future={{ v7_startTransition: true, v7_relativeSplatPath: true }}> {/* מגדיר נתב דפדפן עם תכונות עתידיות של React Router v7 - מעברים חלקים יותר ונתיבים יחסיים */}
      <App />
    </BrowserRouter>
  </StrictMode>,
)
