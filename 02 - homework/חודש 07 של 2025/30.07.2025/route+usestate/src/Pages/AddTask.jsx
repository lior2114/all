import { useState } from "react"
import { useNavigate } from "react-router-dom"

export function AddTask({sendtask}){

    const [task, setTask] = useState("")
    let navigation = useNavigate()
    function btnhandle(){
        if (task.trim() !=="" && task.trim() !=="." ){
            sendtask(task)
            navigation("/Tasks")
        }
    }
    return (
        <>
        <h1>Add Tasks</h1>
        <div>
            <input type="text"
            placeholder="Enter Task"
            onChange={(e) => setTask(e.target.value)}
            />

            <button onClick={btnhandle}>click</button>
        </div>
        </>
    )
}