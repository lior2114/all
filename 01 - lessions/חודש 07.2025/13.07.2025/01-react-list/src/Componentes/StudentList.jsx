export function StudentList() {
    let names = ["Or", "Sergei", "Memo"]
    //1. properties
    //2. functions
    //3. jsx + html

    // <li>Or</li> 
    // <li>Sergei</li>
    // <li>Memo</li>

    let students = names.map((item,index)=><li key = {index}>{item}</li>)

    return (
        <>
            <p>StudentList</p>
            <ul>
                {students}
            </ul>
        </>
    )
}
