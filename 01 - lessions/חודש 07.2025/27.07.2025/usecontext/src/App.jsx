import { useState } from "react"
import CounterContext from "./Contexts/CounterContext"
import { C } from "./Components/c"
import { B } from "./Components/B"
import { A } from "./Components/A"


function App() {
  const [count, setCount] =useState(10)

  return (
    <>
    <div>
      <CounterContext.Provider value={{count, setCount}}>
        <C/>
        <B/>
        <A/>
      </CounterContext.Provider>
    </div>
    </>
  )
}

export default App
