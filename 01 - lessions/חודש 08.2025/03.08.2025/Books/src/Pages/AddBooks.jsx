import { useState } from "react"
import { useBookContext } from "../Contexts/BookContext"
import { useNavigate } from "react-router-dom"

export function AddBooks(){
    const {addBooks} = useBookContext()
    const [bookName, setBookName] = useState("")
    const [authorName, setAuthorName] = useState("")
    const navigation = useNavigate()
    function hndlbtn(){
        if(bookName.trim()==""&&authorName.trim()==""){
            alert("empty values")
        }else{
            addBooks(bookName,authorName)
            navigation("/Books")
        }
    }

    return(
        <>
            <h1>Add to MyBooks</h1>
        <div>
            <input type="text"
            placeholder="Name of the Book"
            onChange={(e)=> setBookName(e.target.value)}
            />
            <br /> <br />
            <input type="text"
            placeholder="Author name"
            onChange={(e)=>setAuthorName(e.target.value)}
            />
            <br /><br />
            <button onClick={hndlbtn}>click</button>
        </div>
        </>
    )
}