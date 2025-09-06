import { CreateTask } from "./Components/Card-1+2/CreateTask"
import { TasksProvider } from "./Contexts/TasksContext"


function App() {


  return (
    <TasksProvider>
      <CreateTask/>
    </TasksProvider>
  )
}

export default App