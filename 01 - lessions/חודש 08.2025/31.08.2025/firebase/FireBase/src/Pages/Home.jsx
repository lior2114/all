import styles from "./Home.module.css";

export function Home(){
    return(
        <div className={styles.container}>
            <h1 className={styles.title}>My Firebase App</h1>
        </div>
    )
}