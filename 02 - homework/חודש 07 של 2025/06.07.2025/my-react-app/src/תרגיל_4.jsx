import { useState } from 'react'
import './App.css'

function App() {
  const [n1, number1] = useState()
  const [n2, number2] = useState()
  const [answer, setAnswer] = useState("answer here")

  function suming(){
    setAnswer(Number(n1)+Number(n2))
  }
  return (
    <>
    <label>number 1: </label>
    <input type="number" 
    value = {n1}
    onChange={(e)=>number1(e.target.value)}
    />
    <br /><br />
    <label>number 2: </label>
    <input type="number" 
    value={n2}
    onChange={(e)=>number2(e.target.value)}
    />
    <br /><br />
    <button onClick={suming}>sum</button>
    <div>{answer}</div>
    </>
  )
}

export default App
