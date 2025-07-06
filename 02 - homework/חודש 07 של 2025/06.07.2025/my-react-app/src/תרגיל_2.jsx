import { use, useState } from 'react'
import './App.css'

function App() {
  const [isVisible, setIsVisible] = useState(true)
  const [message, setMessage] = useState("")

  function switch_modes(){
    if (isVisible === true){
      setIsVisible(false)
    } else if (isVisible === false){
      setIsVisible(true)
    }
  }

  function show(){
    if (isVisible === true){
      setMessage("I am true")
    }else{
      setMessage("")
    }
  }
  return (
    <>
      <button onClick={() =>{switch_modes(); show();}}>click to switch modes</button>
      <br /><br />
      <p >{message}</p>
    </>
  )
}

export default App
