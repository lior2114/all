import { Routes, Route, Link } from 'react-router-dom';
import About from "./Pages/About";
import Home from "./Pages/Home";
import NotFound from "./Pages/NotFound";
import Contact from "./Pages/Contact";



function App() {
  return (
    <>
    <nav style={{display: "flex", flexDirection: "column"}}>
      <Link to="/">Home</Link>
      <br />
      <Link to = "About">About</Link>
      <br />
      <Link to = "Contact">Contact</Link>
      <br />
    </nav>
      <Routes>
        <Route path = "/" element = {<Home/>}></Route>
        <Route path = "About" element = {<About/>}></Route>
        <Route path = "Contact" element = {<Contact/>}></Route>
        <Route path = "*" elemet = {<NotFound/>}></Route>
      </Routes>

    </>
  )
}

export default App;
