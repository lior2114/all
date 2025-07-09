import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './05-App-exe-message.jsx' //כאן משנים לפי השם של הקובץ

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
