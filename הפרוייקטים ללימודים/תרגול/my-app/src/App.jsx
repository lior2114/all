import { Routes, Route } from "react-router-dom"
import { NavBar } from "./Components/NavBar"
import { About } from "./Pages/About"
import { Home } from "./Pages/Home"
import { Login } from "./Pages/Login"
import { Register } from "./Pages/Register"


function App() {


  return (
    <>
    <NavBar/>
    <Routes>
    <Route path = "/" element = {<Home/>}/>
    <Route path = "/About" element = {<About/>}/>
    <Route path = "/Login" element = {<Login/>}/>
    <Route path = "/Register" element = {<Register/>}/>
    </Routes>
    </>
  )
}

export default App
