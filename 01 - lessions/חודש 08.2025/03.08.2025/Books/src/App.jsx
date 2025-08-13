import { NavBar } from "./Components/NavBar";
import { BookProvider } from "./Contexts/BookContext";
import { Routes, Route } from "react-router-dom";
import {Home} from "./Pages/Home";
import {Books} from "./Pages/Books";
import { AddBooks } from "./Pages/AddBooks";

function App() {


  return (
    <>
      <BookProvider>
        <NavBar />
        <Routes>
          <Route path="/" element={<Home />}></Route>
          <Route path="/Books" element={<Books />}></Route>
          <Route path="/AddBooks" element={<AddBooks />}></Route>
        </Routes>
      </BookProvider>
    </>
  )
}

export default App
