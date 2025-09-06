import { Routes, Route } from "react-router-dom"
import Navbar from "./Components/Navbar"
import { Home } from "./Pages/Home"
import Login from "./Pages/Login"
import Register from "./Pages/Register"

function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </>
  )
}

export default App
