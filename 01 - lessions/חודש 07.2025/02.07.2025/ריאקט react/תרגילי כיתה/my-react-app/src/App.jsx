import './App.css'
function App() {
  let country = "israel"
  let city = "givat shmuel"
  let street = "rahavat keren hysod 7"

  function for_alert(){
    alert (country + " " + city + " " + street)
  }


  return (
    <>
      <button onClick={for_alert}>click for display</button>
    </>
  )
}


export default App