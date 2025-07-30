import { useContext, useState } from "react"
import ThemeContext from "../Contexts/ThemeContext"
import styles from './SwitchDorL.module.css'
export function SwitchDorL(){

    const {darklight, setDarkLight} = useContext(ThemeContext)

    function handlebutton(){
        setDarkLight((prev) => !prev)
    }

    const ContainerSwitch = darklight ? styles.darkmode: styles.lightmode

    return(
        <>
        <div className={ContainerSwitch}>
         <button onClick={handlebutton}>click to switch modes</button>
         </div>

        </>
    )
}