import { useState } from 'react'
import './App.css'

function App() {
    const [text, settext ] = useState("")
    const [message, setmessage] = useState("")
    function return_text(){
      if (!text.trim()) {
        setmessage("please enter name")
      } else {
        setmessage(text)
      }
    }
  
  return (
    <>
    <input type="text" 
    value = {text}
    placeholder='enter name'
    onChange={(e)=> settext(e.target.value)}
    />
      <button onClick={return_text} >הצג שם</button>
      <div>{message}</div>
    </>
  )
}

export default App
