import { useState } from "react"
function App() {
  const [counter, setCounter] = useState(0)//0 זה מאיזה מספר זה מתחיל לספור 
  //בנוסף ה usestate מאפס את הדף כל פעם כדי שהקאונטר ישתנה

  function increment() {
    setCounter(counter + 1)
  }

  return (
    <>
      <h1>useState</h1>
      <button onClick={increment}>increment</button>
      <p>{counter}</p>
    </>
  )
} 

export default App
