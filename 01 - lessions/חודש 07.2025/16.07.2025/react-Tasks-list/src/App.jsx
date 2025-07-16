import './App.css'
import { Tasks } from './Components/Tasks'


function App() {
  let missions = [
    {
      title: "shoping", isDone: true
    },
    {
      title: "cleaning", isDone: false
      },
      {
        title: "coding", isDone: true
    }
  ]

  return (
    <>
      <h1>Tasks</h1>
      <Tasks tasks = {missions}/>

    </>
  )
}

export default App
