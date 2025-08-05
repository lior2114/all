import { NavBar } from "./Components/NavBar"
import { Home } from "./Pages/Home"
import { Routes, Route, Link } from "react-router-dom"
import { Login } from "./Pages/Login"
import { Register } from "./Pages/Register"
import { UserProvider } from "./Contexts/UserContext"


function App() {


  return (
    <>
    <p>advance contexts</p>
    <UserProvider>
    <NavBar/>
    <Routes>
      <Route path = "/" element = {<Home/>}></Route>
      <Route path = "Login" element = {<Login/>}></Route>
      <Route path = "Register" element = {<Register/>}></Route>
    </Routes>
    </UserProvider>
    </>
  )
}

export default App
