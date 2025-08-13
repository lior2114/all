import { useBookContext } from "../Contexts/BookContext"


export function Books(){

    const {books, removeBook} = useBookContext()

    return (
        <>
            <h1>My Books</h1>
            {books.length === 0 ? (
                <p>Book List is empty</p>
            ) : (
                <ul>
                    {books.map((book) => (
                        <li key={book.id}>
                            <strong>{book.title}</strong> - {book.author} 
                            <button onClick={() => removeBook(book.id)}>מחק</button>
                        </li>
                    ))}
                </ul>
            )}
        </>
    );
}