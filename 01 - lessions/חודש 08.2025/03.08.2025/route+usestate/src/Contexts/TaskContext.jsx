import { useEffect, useState, useContext, createContext } from "react";


//pharse 1 - create context
const TaskContext = createContext()

//pharse 2 - consume context
//דרך ארוכה
export const useTask = ()=>{ // בדיקה שהוא אכן משתמש בו 
    const context = useContext(TaskContext)
    if (!context){
        throw console.error("TaskContext not used");
    }
    return context
}
//דרך קצרה
// export const useTask = () => useContext(TaskContext) // בדיקה שהוא אכן משתמש בו 

export const TaskProvider = ({children}) =>{
    const [tasks, setTask] = useState([])
    useEffect(()=>{
        const save = localStorage.getItem("tasks")
        if (save){
            setTask(JSON.parse(save))
        }
    },[])

    useEffect(()=>{
        localStorage.setItem("tasks", JSON.stringify(tasks))
    },[tasks]) // רק כאשר טאסק משתנה הוא ישמור אותו שוב פעם אוטומית

    const addTask =(newTask)=>{
        setTask([...tasks,newTask])
    }
    const value = {tasks,addTask}

    return (
        <TaskContext.Provider value={value}>
            {children}
        </TaskContext.Provider>
    )

}