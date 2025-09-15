import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import { UserProvider } from './Contexts/userContext'
import { VacationProvider } from './Contexts/vacationContext'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <UserProvider>
      <VacationProvider>
        <BrowserRouter>
          <App />
        </BrowserRouter>
      </VacationProvider>
    </UserProvider>
  </StrictMode>,
)
