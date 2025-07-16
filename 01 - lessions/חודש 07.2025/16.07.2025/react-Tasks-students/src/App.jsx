import './App.css'
import { Students } from './Components/Students'



function App() {
  let allClass= [
    {
        Fname:"lior" , Lname: "mamo", Grade: 100
    },
      {
        Fname: "sara", Lname: "cohen", Grade: 95
      },
      {
        Fname: "david", Lname: "levi", Grade: 88
      },
      {
        Fname: "davfsid", Lname: "lfsevi", Grade:  30
      }
]

  return (
    <>
      <h1>Students</h1>
      <Students students = {allClass}/>

    </>
  )
}

export default App
