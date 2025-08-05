export function Tasks({gettask}){

    function show(){
        return gettask.map((task,index) => (<li key={index}>{task}</li>))
    }
    return (
        <>
        <h1>Tasks</h1>
        <div>
            {gettask.length ==0 ? <p>List is empty please enter tasks</p> :
            <ul>
                {show()}

            </ul>
            }
        </div>
        </>
    )
}