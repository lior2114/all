export function Book (props){
    function deleteBook(){
        props.PressToDelete(props.BookId)
    }

    return (
        <>
            <div>{props.BookName}  - {props.PublisherName} -{props.BookId}</div>
            <button onClick={deleteBook}>🗑️ מחק</button>
            
        </>
    )
}