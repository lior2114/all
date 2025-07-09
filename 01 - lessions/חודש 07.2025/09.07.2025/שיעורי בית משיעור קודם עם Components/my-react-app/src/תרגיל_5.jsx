import { useState } from 'react'
import './App.css'

function App() {
  const [age, setAge] = useState()
  const[check, setCheck] = useState()

  function check_age(){
    if (age === undefined || age === "" || isNaN(Number(age)) || Number(age) < 0 || Number(age) > 120) {
      setCheck("age is incorrect")
    }
    else if (Number(age) < 18){
      setCheck("to small")
    }else if(Number(age) > 18){
      setCheck("old enough")
    }else{
      setCheck("18 exacly")
    }
  }

  return (
    <>
      <input type="number" 
      value = {age}
      placeholder='Enter your age'
      onChange={(e)=>setAge(e.target.value)}
      />
      <button onClick={check_age}>בדוק</button>
      <div>{check}</div>

    </>
  )
}

export default App
