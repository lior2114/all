import { useState } from "react"
import { useNavigate } from "react-router-dom"
import { useTask } from "../Contexts/TaskContext"

export function AddTask(){

    const [input, setInput] = useState("")
    const {addTask} = useTask()
    let navigation = useNavigate()
    function btnhandle(){
        if (input.trim() !=="" && input.trim() !=="." ){
            addTask(input.trim())
            navigation("/tasks")
        }
    }
    return (
        <>
        <h1>Add Tasks</h1>
        <div>
            <input type="text"
            placeholder="Enter Task"
            onChange={(e) => setInput(e.target.value)}
            />

            <button onClick={btnhandle}>click</button>
        </div>
        </>
    )
}