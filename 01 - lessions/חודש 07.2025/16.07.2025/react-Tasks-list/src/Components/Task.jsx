export function Task(props){


    return(
        <>
        <p>{props.title} - {props.isDone?"Done" : "Not Done"}</p>
        </>
    )
}