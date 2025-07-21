import { useState } from "react"
import { BookList } from "./Components/BookList";

function App() {
  const [books, setBooks] = useState([
    {BookName: "The Great Gatsby", PublisherName: "Scribner", BookId: 1},
    {BookName: "To Kill a Mockingbird", PublisherName: "J.B. Lippincott", BookId: 2},
    {BookName: "1984", PublisherName: "Secker & Warburg", BookId: 3},
    {BookName: "Pride and Prejudice", PublisherName: "T. Egerton", BookId: 4},
    {BookName: "The Hobbit", PublisherName: "Allen & Unwin", BookId: 5}
  ]);


  const deleting = ((e) => {setBooks(books.filter(book => book.BookId !== e))})
  return (
    <>
      <BookList
      books = {books}
      deleting = {deleting}
      />
    </>

  )
}

export default App
