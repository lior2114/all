import { useState } from "react"
import ThemeContext from "./Contexts/ThemeContext"
import { SwitchDorL } from "./Components/SwitchDorL"
import './App.css'
import { Message } from "./Components/Message"

function App() {
  const [darklight, setDarkLight] = useState(false)

  return (
    <>
      <ThemeContext.Provider value={{ darklight, setDarkLight }}>
        <Message />
        <SwitchDorL />
      </ThemeContext.Provider>
    </>
  )  
}

export default App
