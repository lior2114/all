import { useState } from "react"

export function UserNameDisplay(props){
  //1. properties
  const [username, setUsername] = useState("")
  const [text, setText] = useState("")
  //2. functions
  function return_text(){
    if (username.length==0){
        setText(props.emptyMessage)
    }else{
        setText("Hello "+ username)
    }
  }
  //3. js + html
    return(
    <>
    <h1>UserNameDisplay</h1>
    <input type="text"
    onChange={(e)=> setUsername(e.target.value)}
    />
    <button onClick={return_text}>הצג שם</button>
    <div>{text}</div>
    </>
    )
}