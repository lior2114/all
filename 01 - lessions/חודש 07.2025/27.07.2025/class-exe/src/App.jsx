import { useState } from "react"
import { useContext } from "react"
import UserContext from "./Contexts/UserContext"
import { ShowUser } from "./Components/ShowUser"
function App() {
  const [user, setUser] = useState("")

  return(
    <>
        <UserContext.Provider value={{user, setUser}}>
          <ShowUser/>
          <h1>Hello {user}</h1>
          <p>User Name: {user}</p>
        </UserContext.Provider>
    </>
  )
}

export default App
