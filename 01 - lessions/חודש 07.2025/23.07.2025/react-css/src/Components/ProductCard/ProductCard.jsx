import styles from "./ProductCard.module.css"

export function ProductCard({product}){
    return(
        <>
        <div className={styles.card}>
                <h3 className={styles.title}>{product.name}</h3>
                <p>{product.description}</p>
                <button className={styles.btn}>Add to cart</button>

        </div>
        </>
    )
}