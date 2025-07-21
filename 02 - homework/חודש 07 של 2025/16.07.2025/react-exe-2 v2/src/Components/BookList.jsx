import { Book } from "./Book" 
export function BookList(props){
    let book =  props.books.map((book, index)=>{
        return(<Book
        key = {index}
        BookName = {book.BookName}
        PublisherName = {book.PublisherName}
        BookId = {book.BookId}
        PressToDelete = {props.deleting}
        />
        )
    })




    return (
        <>
            <div>{book}</div>
        </>
    )

}