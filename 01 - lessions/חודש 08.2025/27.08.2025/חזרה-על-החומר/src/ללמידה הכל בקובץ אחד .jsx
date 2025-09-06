import { Card, Typography } from '@mui/material';
import { TaskCard } from './Components/Card/TaskCard';
import { useState } from 'react';


    {/* שאלה 1 ו 2  */}
function App() {
  let tasks = [{
    title: "Task1",
    description: "description 1"
  }, {
    title: "Task2", 
    description: "description 2"
  }, {
    title: "Task3",
    description: "description 3"
  }, {
    title: "Task4", 
    description: "description 4"
  }, {
    title: "Task5",
    description: "description 5"
  }]


  {/* שאלה 3  */}
  const [title, setTitle] = useState("")
  const [description, setDescription] = useState("")
  const [newTasks, setNewTasks] = useState([])

  const btlhandle = () => {
    const newTask = {
      title: title,
      description: description
    }
    setNewTasks([...newTasks, newTask])
    setTitle("")
    setDescription("")
  }


  
  return (
    <>
    {/* שאלה 1 ו 2  */}
      <Typography >
        ברוכים הבאים לאפליקצית המשימות שלי
      </Typography>
      <TaskCard title = {tasks[0].title} description= {tasks[0].description}/>
      <TaskCard title = {tasks[1].title} description= {tasks[1].description}/>


{/* שאלה 3  */}
    <label>title: </label>
    <input type="text"
    value={title}
    onChange={(e)=> setTitle(e.target.value)}
    />
    <br/>
      <label>description: </label>
    <input type="text"
    value={description}
    onChange={(e)=> setDescription(e.target.value)}
    />
    <br />
      <button onClick={btlhandle}>
        Add Task
      </button>
      
      {/* הצגת כל המשימות החדשות */}
      {newTasks.length === 0 ? (
        <div>No cards yet</div>
      ) : (
        newTasks.map((task, index) => (
          <TaskCard key={index} title={task.title} description={task.description}/>
        ))
      )}
    </>
  )
}

export default App
