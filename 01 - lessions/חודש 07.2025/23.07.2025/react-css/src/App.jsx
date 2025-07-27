import { ProductCard } from "./Components/ProductCard/ProductCard"
import { ProductList } from "./Components/ProductCard/ProductList"

function App() {

  let p = {
    name:"laptop",
    description: "description description description description "
  }

  let products = [
    { id: 1, name: "Laptop", description: "Lightweig" },
    { id: 2, name: "Headphones", description: "Noise" },
    { id: 3, name: "Smartwatch", description: "Track" }
  ]
  return (
    <>
      {/* <ProductCard
      product = {p}
      /> */}
      <ProductList products={products}/>
    </>
  )
}

export default App
