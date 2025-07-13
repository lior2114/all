export function ProductList(){
    let products = [
        { name: "Apple", price: 45 },
        { name: "Banana", price: 55 },
        { name: "Orange", price: 60 },
        { name: "Milk", price: 80 },
        { name: "Bread", price: 100 }
    ]


    //בשיטה הזאת אנחנו שומרים אותו לתוך משתנה 
    //{item.name + (item.price > 50 ? " יקר" : " זול")}// אפשר גם  להוסיף אחרי הli
    let product = products.map((item,index) => (
        <li key={index}>{item.name} - {item.price} - {item.price > 50 ? 
        <span style ={{color :"red"}}>יקר</span> : <span style ={{color :"green"}}>זול</span>}</li>
    ));



    return(
        <>
        <h1>Products</h1>
            <ul>
                {product} לפעמים נראה גם משורה 11 כאן 
            </ul>
        </>
    )
}