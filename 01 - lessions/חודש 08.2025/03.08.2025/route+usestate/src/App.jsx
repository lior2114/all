import { Home } from "./Pages/Home"
import { Routes, Route, Link } from "react-router-dom"
import { Tasks } from "./Pages/Tasks"
import { AddTask } from "./Pages/AddTask"
import { useState } from "react"
import NavBar from "./Components/NavBar"
import { TaskProvider } from "./Contexts/TaskContext"

function App() {

  return (
    <>
    <TaskProvider>
      <NavBar/>
      <Routes>
        <Route path = "/" element={<Home />}></Route>
        <Route path = "/tasks" element={<Tasks/>}></Route>
        <Route path="/addtask" element={<AddTask />} />
        </Routes>
    </TaskProvider>
    </>
  )
}

export default App
