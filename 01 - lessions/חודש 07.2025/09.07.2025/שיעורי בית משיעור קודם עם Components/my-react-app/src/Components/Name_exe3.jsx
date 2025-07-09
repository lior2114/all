import React, { useState } from "react";

export function Name_Check() {
    const [text, settext ] = useState("")
    const [message, setmessage] = useState("")
    function return_text(){
      if (!text.trim() || !isNaN(text)) {
        setmessage("please enter name")
      } else {
        setmessage(text)
      }
    }
  
  return (
    <>
    <input type="text" 
    value = {text}
    placeholder='enter name'
    onChange={(e)=> settext(e.target.value)}
    />
      <button onClick={return_text} >הצג שם</button>
      <div>{message}</div>
    </>
  )
}