import { Usercard } from "./Components/UserCard/UserCard"


function App() {
  let users = [
   {username: "lior", email: "lior@email.com"},
   {username: "david", email: "david@email.com"},
   {username: "sarah", email: "sarah@email.com"},
   {username: "michael", email: "michael@email.com"},
   {username: "rachel", email: "rachel@email.com"}
  ]

  return (
    <>
    <h1>User Info</h1>
      {users.map((user) => <Usercard userInfo={user}/>)}
    </>
  )
}

export default App
