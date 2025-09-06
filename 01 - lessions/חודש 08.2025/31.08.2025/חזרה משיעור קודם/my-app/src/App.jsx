import TaskCard from './components/Card/TaskCard'
import { useState } from 'react'
import Tasks from './components/Tasks/Tasks'
import { TaskProvider } from './contexts/TaskContext'
function App() {
  return (
    <>
    <div>tasks</div>
    <TaskProvider>
        <Tasks />
    </TaskProvider>

    </>
  )
}

export default App
