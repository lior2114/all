import { useState } from "react"
export function ConditionalGreeting(){
    const [isMorning, setIsMorning] = useState(true)

//v1
    // const [message, setMessage] = useState("")
    // function show(){
    //     if (isMorning === true){
    //         setMessage("בוקר טוב 🌅")
    //         setIsMorning(false)
    //     }else{
    //         setMessage("ערב טוב 🌇")
    //          setIsMorning(true)
    //     }
    // }

    // return(
    //     <>
    //     <h1>Exe 10 - ConditionalGreeting</h1>
    //     <button onClick={show}>הצג ברכה</button>
    //     <div>{message}</div>
    //     </>
    // )


    //v2
    function swiching(){
        setIsMorning((prev)=> !prev)
    }
    
    return(
        <>
       <h1>Exe 10 - ConditionalGreeting</h1>
       <button onClick={swiching}>שנה ברכה</button>
       <div>{isMorning === true ? "בוקר טוב 🌅" : "ערב טוב 🌇"}</div> אפשר גם בלי הטרו
        </>

    )

}