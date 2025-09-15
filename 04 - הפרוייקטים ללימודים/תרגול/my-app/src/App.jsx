import { Routes, Route } from "react-router-dom"
import { NavBar } from "./Components/NavBar"
import { About } from "./Pages/About"
import { Home } from "./Pages/Home"
import { Login } from "./Pages/Login"
import { Register } from "./Pages/Register"
import { Vacations } from "./Pages/vacations"
import { CreateVacation} from "./Pages/createVacation"


function App() {


  return (
    <>
    <NavBar/>
    <Routes>
    <Route path = "/" element = {<Home/>}/>
    <Route path = "/About" element = {<About/>}/>
    <Route path = "/Login" element = {<Login/>}/>
    <Route path = "/Register" element = {<Register/>}/>
    <Route path = "/vacations" element = {<Vacations/>}/>
    <Route path = "/createVacation" element = {<CreateVacation/>}/>
    </Routes>
    </>
  )
}

export default App
