import { vacationscard } from "../Components/vacationCard"
import styles from "../Components/vacationCard.module.css"

export function Vacations() {
    return (
        <div className={styles.pageContainer}>
            {vacationscard()}
        </div>
    )
}