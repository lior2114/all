import { useState } from "react"
import styles from './UserCard.module.css'

export function Usercard({userInfo}){

    return (
        <>
        <div className={styles.all}>
            <p className={styles.p}>{userInfo.username}</p>
            <p className={styles.p}>{userInfo.email}</p>
        </div>

        <button className={styles.btn}>שלח הודעה</button>
        </>
    )
}