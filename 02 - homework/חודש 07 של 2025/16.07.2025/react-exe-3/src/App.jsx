import { StudentList } from "./Components/StudentList"
function App() {
  let studentclass = [
    {Fname: "lior", Lname: "mamo", Grade: 100},
    {Fname: "lior", Lname: "mamo", Grade: 95},
    {Fname: "Daniel", Lname: "Cohen", Grade: 95},
    {Fname: "Sarah", Lname: "Levy", Grade: 50},
    {Fname: "Michael", Lname: "Ben", Grade: 92},
    {Fname: "Rachel", Lname: "Goldstein", Grade: 55},
    {Fname: "David", Lname: "Avraham", Grade: 65}
  ]
  

  return (
    <>
    <h1>search bar</h1>
      <StudentList
      student = {studentclass}
      />
    </>

  )
}

export default App
