import { Children, createContext, useContext, useEffect, useState } from "react";

const BookContext = createContext();

export const useBookContext = () => {
    const test = useContext(BookContext)
    if (!test) {
        throw console.error("You need to use BookContext");
    }
    return test
}

export const BookProvider = ({ children }) => {
    const [books, setBooks] = useState([])
    const [isInitialized, setIsInitialized] = useState(false)

    // טעינה מ-localStorage בהתחלה
    useEffect(() => { //מרדנר אותם פעם ראשונה
        const savedBooks = localStorage.getItem("books")
        if (savedBooks) {
            setBooks(JSON.parse(savedBooks))
            setIsInitialized(true)
        }else{
            setIsInitialized(false)
        }
    }, [])

    
    // שמירה ל-localStorage כשהספרים משתנים
    useEffect(() => { //אחרי כל שינוי מרנדר מחדש ומגדיר אותם מחדש
        if (isInitialized) {
            localStorage.setItem("books", JSON.stringify(books))
        }
    }, [books, isInitialized])

    const addBooks = (bookName, authorName) => {
        const newBook = {
            id: Date.now(),
            title: bookName,
            author: authorName
        }
        setBooks([...books, newBook])
    }

    const removeBook = (id) => {
        setBooks(books.filter(book => book.id !== id))
    }

    const value = {
        books,
        addBooks,
        removeBook
    }

    return (
        <BookContext.Provider value={value}>
            {children}
        </BookContext.Provider>
    )

}
