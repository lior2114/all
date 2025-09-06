import { Card, Typography, CardContent} from '@mui/material';
import styles from './TaskCard.module.css';

export function TaskCard({ id, title, description, done, onToggle, onToggleDelete }){
    return(
        <Card className={styles.card}>
            <CardContent>
                <Typography 
                    variant="h6" 
                    component="div" 
                    className={`${styles.title} ${done ? styles.completed : styles.pending}`}
                >
                    {title}
                </Typography>
                <Typography 
                    variant="body2" 
                    component="div"
                    className={styles.description}
                >
                    {description}
                </Typography>
                <div className={styles.checkboxContainer}>
                    <input 
                        type="checkbox" 
                        checked={done} 
                        onChange={() => onToggle(id)}
                        className={styles.checkbox}
                    />
                    <label className={styles.label}> {done ? 'Completed' : 'Pending'}</label>
                </div>

                <button onClick={() => onToggleDelete(id)}>
                    Delete
                </button>
            </CardContent>
        </Card>
    )
}