import Home from "./Pages/Home"
import { Routes, Route, Link } from "react-router-dom"
import AddTask from "./Pages/AddTask"
import Tasks from "./Pages/Tasks"
import { useState } from "react"



function App() {
    const [tasks, setTasks] = useState([])

    const addTask = (newTask) => {
      setTasks([...tasks, newTask])
    }
  return (
    <>
    <nav>
      <Link to="/">Home</Link>
      <br />
      <Link to="/AddTask">AddTask</Link>
      <br />
      <Link to="/Tasks">Tasks</Link>
    </nav>
    <Routes>
      <Route path="/" element={<Home/>}></Route>
      <Route path="/AddTask" element={<AddTask addTask={addTask}/>}></Route>
      <Route path="/Tasks" element={<Tasks tasks={tasks}/>}></Route>
    </Routes>
    </>
  )
}

export default App
