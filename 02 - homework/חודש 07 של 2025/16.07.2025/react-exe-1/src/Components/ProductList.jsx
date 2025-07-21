import { Product } from "./Product"
export function ProductList(props){
    let Products = props.Products.map((product) => {
        return <Product
        Pname = {product.Pname}
        Price = {product.Price}
        />
    })



    return (
        <>
        {Products}
        </>
    )

}