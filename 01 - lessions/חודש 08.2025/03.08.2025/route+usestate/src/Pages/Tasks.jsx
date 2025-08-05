import { useTask } from "../Contexts/TaskContext"

export function Tasks(){
    const {tasks} = useTask()
    return (
        <>
        <h1>Tasks</h1>
        <div>
            {tasks.length ==0 ? <p>List is empty please enter tasks</p> :
            <ul>
                {tasks.map((task,index)=><li key={index}>{task}</li>)}

            </ul>
            }
        </div>
        </>
    )
}