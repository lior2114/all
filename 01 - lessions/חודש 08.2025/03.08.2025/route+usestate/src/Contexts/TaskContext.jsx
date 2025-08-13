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
    const [isInitialized, setIsInitialized] = useState(false) // (יפתור לנו את הבעיה שזה (עובד סינכרוני הכוונה שהכל עובד במכה 
    useEffect(()=>{
        const save = localStorage.getItem("tasks")
        if (save){
            setTask(JSON.parse(save))
            setIsInitialized(true) //ורק שזה מופעל היוסאפפקט הבא גם יופעל 
        }
    },[])

    useEffect(()=>{
        if(isInitialized){ // אם נכון אז הוא ירוץ אם לא הוא לא ככה שאם נאפס את הדף הוא לא ירוץ וישמור מערך ריק ונמשיך לראות את המשימות 
        localStorage.setItem("tasks", JSON.stringify(tasks))} // המרה למחרוזת 
    },[tasks, isInitialized]) // רק כאשר טאסק משתנה והאינישילייז נכנס לפעולה אז הוא ישמור אותו שוב פעם אוטומית

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