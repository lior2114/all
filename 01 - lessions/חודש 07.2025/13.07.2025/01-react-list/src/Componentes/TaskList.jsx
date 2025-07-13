export function TaskList(){
    let tasks = [
        {title: "Morning", Done: true},
        {title: "Afternoon", Done: false},
        {title: "Evning", Done: true}
    ];

    let check_tasks = tasks.map((item, index)=>
         <li key = {index}>{item.title} - {item.Done === true ? "✅":"❌"}</li>)


    return(
        <>
        <h1>TaskList</h1>
            <ul>
                {check_tasks}
            </ul>
        </>
    )
}