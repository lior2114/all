import { useState } from "react"

export function Weather(){
//v1
    // const [israin, setIsrain] = useState(true)
    // const [message, setMessage] = useState()
    // function switching(){
    //     if (israin === true){
    //         setMessage("תישאר בבית ☔️)
    //         setIsrain(false)
    //     }else{
    //         setMessage("צא החוצה ☀️)
    //         setIsrain(true)
    //     }
    // }

    // return(
    //     <>
    //         <button onClick={switching}>switch modes</button>
    //         <div>{message}</div>
    //     </>
    // )}

//V2
    const [isRaining, setIsRaining] = useState(true);

    function toggleRain() {
        setIsRaining((prev) => !prev);// מחליף את המצב למצב שונה ממה שקיים 
    } 

    return (
        <>
            <button onClick={toggleRain}>החלף מצב גשם</button>
            <div>
                {isRaining ? "תישאר בבית ☔️" : "צא החוצה ☀️"}
            </div>
        </>
    )}