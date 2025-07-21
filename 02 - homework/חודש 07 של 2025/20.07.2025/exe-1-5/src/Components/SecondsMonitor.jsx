import { useEffect, useState } from "react"

export function SecondsMonitor(){

    const [timer, setTimer]= useState(0)
    
    useEffect(()=>{
        const time = setInterval(() => {
            setTimer((prev)=> prev+1)
        }, 1000);
        return ()=> clearInterval(time)
    },[])

    return(
        <>
            <div>עברו {timer} שניות</div>
            <button onClick={()=> setTimer(0)}>click to reset seconds</button>
        </>
    )
}