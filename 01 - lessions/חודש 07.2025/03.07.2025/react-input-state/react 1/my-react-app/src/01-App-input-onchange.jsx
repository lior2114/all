function App() {
  function clicked(element) {
    //alert("input clicked")
    //console.log(e.target)// html element
    console.log(element.target)
  }

  function firstNameChange() {
    console.log("first name changed")
  }

  return (
    <>
      <h1>input</h1>
      <input
        type="text"
        placeholder="firstname"
        onChange={clicked}
      />
    </>
  )
}

export default App
