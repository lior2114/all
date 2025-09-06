import { useState } from "react"
import TaskCard from "../Card/TaskCard"
import { useTaskContext } from "../../contexts/TaskContext"
import styles from "./Tasks.module.css"

export default function Tasks(){
    const { tasks, addTask, toggleComplete, deleteTask } = useTaskContext()
    const [task, setTask] = useState({id:0, title:"", description:"", isDone:false})
    
    function handleAddTask(){ 
        if (task.title.trim() && task.description.trim()) {
            addTask({
                title: task.title.trim(),
                description: task.description.trim()
            })
            setTask({id:0, title:"", description:"", isDone:false})
        }
    }
    
    function handleChange(e){
        setTask({...task, [e.target.name] : e.target.value})
    }

    function handleToggleDone(taskId) {
        toggleComplete(taskId)
    }
    
    function handleDelete(taskId){
        deleteTask(taskId)
    }

    return (
        <div className={styles.tasksContainer}>
            <div className={styles.header}>
                <h1 className={styles.title}>My Tasks</h1>
                <p className={styles.subtitle}>Organize your day with beautiful task cards</p>
            </div>
            
            <div className={styles.inputSection}>
                <div className={styles.inputGroup}>
                    <input 
                        type="text" 
                        name="title" 
                        placeholder="Task Title" 
                        value={task.title}
                        onChange={handleChange}
                        className={styles.input}
                    />
                    <input 
                        type="text" 
                        name="description" 
                        placeholder="Task Description" 
                        value={task.description}
                        onChange={handleChange}
                        className={styles.input}
                    />
                </div>
                <button 
                    onClick={handleAddTask}
                    className={styles.addButton}
                    disabled={!task.title.trim() || !task.description.trim()}
                >
                    + Add Task
                </button>
            </div>
            
            <div className={styles.tasksList}>
                {tasks.length > 0 ? (
                    tasks.map((task) => (
                        <TaskCard 
                            key={task.id} 
                            id={task.id}
                            title={task.title} 
                            description={task.description} 
                            isDone={task.isDone}
                            onToggleDone={handleToggleDone}
                            onDelete={handleDelete}
                        />
                    ))
                ) : (
                    <div className={styles.noTasks}>
                        <div className={styles.noTasksIcon}>📝</div>
                        <h3>No tasks yet</h3>
                        <p>Start by adding your first task above!</p>
                    </div>
                )}
            </div>
        </div>
    )
}