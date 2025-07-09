import { useState } from "react"
function App() {
  //let firstname = "Mamo";// חשבון רגיל
  const [firstname, setFirstName] = useState("Mamo") // חשבון עם useState

  function firstNameChanged(e) {
    //console.log(e.target.value)
    //firstname = e.target.value;
    //console.log(firstname)
    setFirstName(e.target.value)
  }

  return (
    <>
      <h1>Input State Example</h1>
      <input
        type="text"
        value={firstname}//הטקסט בפנים 
        placeholder="First Name"
        onChange={firstNameChanged}
      />
      <br /><br />
      <p>{firstname}</p>
    </>
  )
}

export default App
