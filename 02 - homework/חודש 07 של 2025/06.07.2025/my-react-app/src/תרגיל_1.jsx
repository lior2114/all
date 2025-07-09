import { useState } from 'react'
import './App.css'

function App() {
  const [message, setMessage] = useState("Hello")
  function toggleMessage(){
    if(message === "Hello"){
      setMessage("GoodBye")
    }
    else{
      setMessage("Hello")
    }
  }

  return (
    <>
      <h1>useState</h1>
      <button onClick={toggleMessage}>toggle</button>
      <p>{message}</p>
    </>
  )
}

export default App
