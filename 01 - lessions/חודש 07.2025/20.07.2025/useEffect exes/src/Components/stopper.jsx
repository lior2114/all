import { useEffect, useState } from "react"

export function Stopper(){
    const [time, setTime] = useState(10)



    useEffect(() =>{
        const timer = setInterval(() => {
            setTime(prev => {
                if (prev === 1) {
                    clearInterval(timer)
                }
                return prev-1
            })
        }, 1000);
        return () => clearInterval(timer)
    }, [])




    return(
        <>
                <div>
                <h2>stopper</h2>
                {time}
                </div>
        </>
    )
}