export function MovieRatings(){
    let movies = [
        {title: "spiderman home coming", rating: 10},
        {title: "inception", rating: 5},
        {title: "the matrix", rating: 2},
        {title: "interstellar", rating: 10}
    ]

    let mapMovies = movies.map((check, index)=> 
    <li key = {index}>{check.title} - {check.rating} {check.rating > 8 ? "מומלץ מאוד" : "רגיל"}</li>)


    return(
        <>
        <h1>Exe 8 - MovieRatings</h1>
        <div>{mapMovies}</div>
        </>
    )
}