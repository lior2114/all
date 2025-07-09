import { useState } from 'react'
import './App.css'

function App() {
    const [password1, setPassword1] = useState()
    const [password2, setPassword2] = useState()
    const [check, Setcheck] = useState()

    function check_Password(){
      if (password1 === password2){
        Setcheck("passwords are matches :)")
      }else{
        Setcheck("password dont matches try again")
      }
    }
  return (
    <>
    <label>Password :</label>
    <input type="password"
    value = {password1}
    onChange={(e)=> setPassword1(e.target.value)}
    />
    <br /><br />
    <label>Repeat Password :</label>
    <input type="password" 
    value = {password2}
    onChange={(e)=> setPassword2(e.target.value)}
    />
    <br /><br />
    <button onClick={check_Password}>בדוק התאמה</button>
    <div>{check}</div>
    </>
  )
}

export default App
