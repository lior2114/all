import { createContext, useState, useEffect } from "react";

const BookContext = createContext()

export const BookProvider = ({ children }) => {
  // טעינת ספרים מ-localStorage או יצירת מערך ריק
  const [books, setBooks] = useState(() => {
    const savedBooks = localStorage.getItem("books");
    return savedBooks ? JSON.parse(savedBooks) : [];
  });

  // שמירה ב-localStorage כשהמערך משתנה
  useEffect(() => {
    localStorage.setItem("books", JSON.stringify(books));
  }, [books]);

  // פונקציה להוספת ספר חדש
  const addBook = (newBook) => {
    const bookWithId = {
      id: Date.now(), // יצירת ID ייחודי
      ...newBook
    };
    setBooks(prevBooks => [...prevBooks, bookWithId]);
  };

  // פונקציה למחיקת ספר
  const deleteBook = (bookId) => {
    setBooks(prevBooks => prevBooks.filter(book => book.id !== bookId));
  };

  // הערכים שנעביר לכל הקומפוננטות
  const contextValue = {
    books,
    addBook,
    deleteBook
  };

  return (
    <BookContext.Provider value={contextValue}>
      {children}
    </BookContext.Provider>
  );
};

export default BookContext