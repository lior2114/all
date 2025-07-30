import { useState } from "react"
import { useNavigate } from "react-router-dom"

export default function AddTask({ addTask }){
    const [newtask, setNewTask] = useState("")
    const navigate = useNavigate()
    
    const handleSubmit = (e) => {
        e.preventDefault()
        if (newtask.trim() !== "" && newtask.trim() !== ".") {
            addTask(newtask)
            navigate("/tasks")
        }
    }
    
    return(
        <div>
            <h2>Add Task</h2>
                <input 
                    type="text"
                    placeholder="הכנס משימה חדשה"
                    value={newtask}
                    onChange={(e) => setNewTask(e.target.value)}
                />
                <button type="submit" onClick={handleSubmit}>הוסף משימה</button>
        </div>
    )
}
