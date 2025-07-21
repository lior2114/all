import { Book } from "./Book" 
export function BookList(props){
    let books = props.books.map((book)=>{
        return <Book
        key={book.id}
        id={book.id}
        BookName = {book.BookName}
        WriterName = {book.WriterName}
        onDelete = {props.onDeleteBook}
        />
    })



    return (
        <>
            <div>{books}</div>
        </>
    )

}