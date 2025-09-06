import { TaskCard } from '../Components/Card-1+2/TaskCard';
import { useState } from 'react';

export function Tasks() {

    const [title, setTitle] = useState("")
    const [description, setDescription] = useState("")
    const [newTasks, setNewTasks] = useState([])
    const [loading, setLoading] = useState(false)
  
    const btlhandle = () => {
      const newTask = {
        id: Date.now(), // יצירת ID ייחודי
        title: title,
        description: description,
        done: false
      }
      setNewTasks([...newTasks, newTask])
      setTitle("")
      setDescription("")
    }

    const toggleTaskStatus = (taskId) => {
      setNewTasks(newTasks.map(task => 
        task.id === taskId ? { ...task, done: !task.done } : task
      ))
    }

    const handleDelete = (taskId) => {
        setNewTasks(newTasks.filter((task) => task.id !== taskId))
    }
    return (
        <>
            {/* שאלה 3  */}
            <label>title: </label>
            <input type="text"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
            />
            <br />
            <label>description: </label>
            <input type="text"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
            />
            <br />
            <button onClick={btlhandle}>
                Add Task
            </button>

            {/* הצגת כל המשימות החדשות */}
            {newTasks.length === 0 ? (
                <div>No cards yet</div>
            ) : (
                newTasks.map((task) => (
                    <TaskCard 
                        key={task.id} 
                        id={task.id}
                        title={task.title} 
                        description={task.description}
                        done={task.done}
                        onToggle={toggleTaskStatus}
                        onToggleDelete = {handleDelete}
                    />
                ))
            )}
        </>
    )
}