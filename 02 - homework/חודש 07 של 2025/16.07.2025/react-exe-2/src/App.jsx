import { useState } from "react"
import { BookList } from "./Components/BookList"


function App() {
  const [books, setBooks] = useState([
    {
      id: 1,
      BookName: "To Kill a Mockingbird", WriterName: "Harper Lee"
    },
    {
      id: 2,
      BookName: "1984", WriterName: "George Orwell"
    },
    {
      id: 3,
      BookName: "Pride and Prejudice", WriterName: "Jane Austen"
    }
  ])

  const deleteBook = (e) => {// מקבל את האיי די שלחצתי עליו את המחיקה
    setBooks(books.filter(book => book.id !== e)) //אם אותו איי די שווה לאיי די ששלחנו אז התנאי לא מתקיים והוא לא מחזיר אותו לפילטר שלא מחזיר אותו חזרה לתוך הרשימה 
  }

  return (
    <>
        <BookList
        books = {books}
        onDeleteBook = {deleteBook}
        />
    </>

  )
}

export default App
