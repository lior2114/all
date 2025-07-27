import styles from "./ProductList.module.css"
import {ProductCard} from "./ProductCard"

export function ProductList({products}) {
    return (
        <div>
            <h2>Our Products</h2>
            <div className={styles.fordiv}> 
                {products.map((product) => (
                    <ProductCard key={product.id} product={product} />
                ))}
            </div>
        </div>
    )
}