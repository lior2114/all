export function FavoriteColors() {
    const colors = ["blue", "green", "purple", "red"];


    //&& אומר אם זה נכון או לא 
    return (
        <>
        <h1>Exe 6 - FavoriteColors</h1>
        {colors.map((color, index) =>
        <button key = {index}> {color} 
        {color == "blue" && "- Cool Color 😎" }
        </button>)}
        </>
    );
}
