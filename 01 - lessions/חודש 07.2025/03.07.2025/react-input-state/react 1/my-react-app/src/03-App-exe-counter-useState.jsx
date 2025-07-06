import { useState } from "react"
function App() {
  const [count, setCounter] = useState(0)

  function increase_count() {
    setCounter(count + 1)
  }
  function decrease_counter() {
    setCounter(count - 1)
  }
  function reset_counter() {
    setCounter(0)
  }
  return (
    <>
      <h1>The Counter</h1>
      <button onClick={increase_count}>click to increase</button>
      <br /> <br />
      <button onClick={decrease_counter}>click to decrease</button>
      <br /> <br />
      <button onClick={reset_counter}>reset counter</button>
      <br /><br />
      <input
        type="text"
        value={count}
        onChange={e => setCounter(Number(e.target.value) || 0)}
      />
      <br /><br />
      <p1>{count}</p1>
    </>
  )
} 

export default App
