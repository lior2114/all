import { useEffect, useState } from "react"

export function MouseMovment(){

    const [x,setX] =useState()
    const [y, setY] = useState()

    useEffect(() => {
        const handleMouseMove = (event) => {
            setX(event.clientX);
            setY(event.clientY);
        };
        
        window.addEventListener('mousemove', handleMouseMove);
        
        return () => {
            window.removeEventListener('mousemove', handleMouseMove);
        };
    }, []);

const mouse = "X: " + (x || 0) + ", Y: " + (y || 0);


    return(
        <>
        <div>{mouse}</div>
        </>
    )
}