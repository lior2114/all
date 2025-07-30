import { useContext } from "react"
import ThemeContext from "../Contexts/ThemeContext"

export function Message(){

    const {darklight} = useContext(ThemeContext)
    let message = darklight ? "Dark Mode" : "Light Mode"

    return(
    <>
        <div style={{
            color:"red", 
            fontSize: "18px", 
            fontWeight: "bold", 
            textAlign: "center", 
            margin: "20px",
            border: "2px solid blue",
            padding: "10px",
            backgroundColor: "yellow",
            position: "fixed",
            top: "20px",
            left: "50%",
            transform: "translateX(-50%)",
            zIndex: 1000
        }}>
            {message} :מצב נוכחי
        </div>
    </>
    )
}