import { Home } from "./Pages/Home"
import { Routes, Route, Link } from "react-router-dom"
import { Tasks } from "./Pages/Tasks"
import { AddTask } from "./Pages/AddTask"
import { useState } from "react"

function App() {
  const [tasks, setTasks] = useState([])

  const showTask = (newTask) => setTasks([...tasks, newTask])
  return (
    <>
      <nav>
        <Link to="Home">Home</Link>
        <br />
        <Link to="Tasks">Tasks</Link>
        <br />
        <Link to="AddTask">Add Task</Link>
      </nav>
      <Routes>
        <Route path = "Home" element={<Home />}></Route>
        <Route path = "Tasks" element={<Tasks gettask={tasks}/>}></Route>
        <Route path="AddTask" element={<AddTask sendtask={showTask} />} /></Routes>
    </>
  )
}

export default App
