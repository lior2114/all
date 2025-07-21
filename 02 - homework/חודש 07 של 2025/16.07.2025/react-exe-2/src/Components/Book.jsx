export function Book (props){
    function handleDelete(){
        props.onDelete(props.id)
    }

    return (
        <>
            <p>{props.BookName} - {props.WriterName} - {props.id}
                <button onClick={handleDelete}>🗑️ מחק</button>
                 </p>
            
        </>
    )
}