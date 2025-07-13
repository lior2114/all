export function ProductListV2(){
    let products = [
        { name: "Apple", price: 45 },
        { name: "Banana", price: 55 },
        { name: "Orange", price: 60 },
        { name: "Milk", price: 80 },
        { name: "Bread", price: 100 }
    ]


    //בשיטה הזאת אנחנו ישר מרנדים את זה בתוך הדף
    return(
        <>
        <h1>Products</h1>
            <ul>
            {products.map((item,index) => (
            <li key={index}>{item.name} - {item.price} - {item.price > 50 ? 
            <span style ={{color :"red"}}>יקר</span> : <span style ={{color :"green"}}>זול</span>}</li>
            ))}
            </ul>
        </>
    )
}