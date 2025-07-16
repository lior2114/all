export function ScoreList(){

    let students = [
        { name: "lior", score: 100 },
        { name: "dan", score: 85 },
        { name: "maya", score: 92 },
        { name: "noa", score: 78 }
    ]

    let mapingStudents = students.map((check, index) => 
    <li key = {index}>{check.name} - {check.score} {check.score > 90 ? "- מצטיין" : ""}</li>)


    return(
        <>  
        <h1>Exe 7 - ScoreList</h1>
        <div>{mapingStudents}</div>
        </>
    )
}