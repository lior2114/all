import { Routes, Route } from "react-router-dom"
import { UserProvider } from "./Contexts/userContext"
import { NavBar } from "./Components/Navbar"
import { About } from "./Pages/About"
import { Home } from "./Pages/Home"
import { Login } from "./Pages/Login"
import { Register } from "./Pages/Register"


function App() {


  return (
    <UserProvider>
      <NavBar/>
      <Routes>
        <Route path = "/" element = {<Home/>}/>
        <Route path = "/About" element = {<About/>}/>
        <Route path = "/Login" element = {<Login/>}/>
        <Route path = "/Register" element = {<Register/>}/>
      </Routes>
    </UserProvider>
  )
}

export default App
