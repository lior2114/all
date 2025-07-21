import { ProductList } from "./Components/ProductList"

function App() {
  let products = [
    {
      Pname: "laptop", Price: 1000
    },
    {
      Pname: "phone", Price: 500
    },
    {
      Pname: "tablet", Price: 700
    }
  ]

  return (
    <>
      <ProductList
      Products = {products}
      />
    </>

  )
}

export default App
