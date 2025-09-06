import styles from './TaskCard.module.css'
 
export default function TaskCard({ id, title, description, isDone, onToggleDone, onDelete }) {
    return (
        <div className={styles.card}>
            <div className={styles.title}>
                <span style={{textDecoration: isDone ? 'line-through' : 'none'}}>
                    {title}
                </span>
            </div>
            <div className={styles.description}>{description}</div>
            <input 
                type="checkbox" 
                className={styles.checkbox} 
                checked={isDone} 
                onChange={() => onToggleDone(id)}
            />
            <button onClick={() => onDelete(id)}>Delete</button>
        </div>
    )
}