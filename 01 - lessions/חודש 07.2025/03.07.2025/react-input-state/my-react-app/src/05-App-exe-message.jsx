import { useState } from "react"
function App() {
  const [message, setmessage] = useState("Hello")
  function change_message(e){
    setmessage(e.target.value)
  }
  function changing(){
    if (message == "Hello"){
      setmessage("GoodBye")
    }else{
      setmessage("Hello")
    }
  }

  return (
    <>
    <h1>Exe 1 messages</h1>
    <h2>{message}</h2>
    <input type="text"
    value = {message}
    onChange={change_message}//אחראי על אירוע של אם יש שינוי מסויים ובהתאם לזה יהיה אפשר להגיב 
    />
      <button onClick={changing}>click</button>
    </>
  )
}

export default App
