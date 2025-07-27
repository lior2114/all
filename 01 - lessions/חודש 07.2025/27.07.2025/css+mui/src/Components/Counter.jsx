import { useState } from "react"
import styles from './Counter.module.css'

export function Counter(){
    const [count, setCounter] = useState(0)
    function up(){
        setCounter((prev) => prev + 1)
    }

    function down(){
        setCounter((prev) => prev <= 0 ? 0:prev -1)
    }
     
    function reset(){
        setCounter(0)
    }

    return(
        <>
        <div className={styles.all}>
            <div className={styles.alldiv}>
                <button className={styles.btn} onClick={up}>up</button>
                <button className={styles.btn} onClick={down}>down</button>
                <button className={styles.reset} onClick={reset}>reset</button>
                <p className={styles.showcount}>{count}</p>
            </div>
        </div>
        </>
    )
}