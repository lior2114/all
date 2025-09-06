import { useState } from "react";
import TaskCard from "../Card/TaskCard";

export default function Tasks(){
    const [tasks, setTasks] = useState([]);
    const [newTask, setNewTask] = useState({title:"", description:""});
    
    function handleAddTask(){
        setTasks([...tasks, newTask]);
        setNewTask({title:"", description:""});
    }
    
    function handleChange(e){
        setNewTask({...newTask, [e.target.name]: e.target.value});
    }
    
    // add and remove operators
    
    return (
        <div>
            <h1>Tasks:</h1>
            <input type="text" name="title" placeholder="Title" onChange={handleChange} />
            <input type="text" name="description" placeholder="Description" onChange={handleChange} />
            <button onClick={handleAddTask}>Add Task</button>
            {tasks.length === 0 ? 
            (<div>No tasks yet</div>) : 
            (tasks.map((task, index) => 
                <TaskCard key={index} title={task.title} description={task.description} />
            ))}
        </div>
    );
}

