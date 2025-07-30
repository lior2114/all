import { useState } from "react"
import UserContext from "./Contexts/usercontext"
import { User } from "./Components/user"
import { ShowUser } from "./Components/ShowUser"


function App() {
  const [user, setUser] = useState("")

  return (
    <>
      <UserContext.Provider value={{user, setUser}}>
        {/* //אפשר שיהיה כאן גם עוד context והוא יכול להיות אחד בתוך השני  */}
      <User/>
      <ShowUser/>
      </UserContext.Provider>
    </>
  )
}

export default App
