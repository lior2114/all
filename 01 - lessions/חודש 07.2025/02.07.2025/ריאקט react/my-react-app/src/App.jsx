import './App.css'

function App() {
  let firstName = "Ariel"
  let lastName = "Gev"

  function displayFirstName() {
    alert(firstName + " " + lastName)
  }

  return (
    <>
      <p>hello world {firstName} {lastName}</p>
      <input type="text" />
      <button onClick={displayFirstName}>display name</button>
    </>
  )
}


export default App