import { useEffect, useState } from "react"

export function BackTimer(){

    let timereturn = 3
    const [time, setTimer] = useState(3)
    const [message, setMessage] = useState("")
useEffect(() => {
    const timer = setInterval(() => {
        setTimer((prev) => {
            if (prev === 1) {
                setMessage(" time is over");
                clearInterval(timer);
            }
            return prev - 1;
    
        });
    }, 1000);
    return () => clearInterval(timer);
}, [time==timereturn]);



    return(
        <>
        <div>
        {time ? time : ""} 
        {message}
        </div>
        <button onClick={()=> {setTimer(timereturn); setMessage("")}}>click</button>

        </>
    )
}