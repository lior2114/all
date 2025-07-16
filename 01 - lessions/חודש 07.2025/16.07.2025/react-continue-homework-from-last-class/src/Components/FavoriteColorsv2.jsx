export function FavoriteColors() {
    const colors = ["Red", "Blue", "Brown"];
    let mapList = colors.map((color, index) => (
        <button key={index}   style={{margin: "10px"}}>
        {color} {color === "Blue" && "- Cool Color 😎"}</button>
    ));
    return (
        <ul>
            {mapList}
        </ul>
    );
}