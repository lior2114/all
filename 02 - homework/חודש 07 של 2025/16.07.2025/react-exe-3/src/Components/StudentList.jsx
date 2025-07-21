import { useState } from "react"
import { Student } from "./Student"
export function StudentList(props){
    const [searchName, setSearchName] = useState("")
    const [searchGrade, setSearchGrade] = useState("")
    
    const filterfieldstudents = props.student.filter((student) => {
        let fullName = student.Fname + " " + student.Lname
        let grade = student.Grade
        let byname = fullName.toLowerCase().includes(searchName.toLowerCase())// מחזיר נכון ולא נכון 
        let bygrade = searchGrade !== "" ? grade == Number(searchGrade) : false
        
        // אם שניהם נכונים 
        if (searchName && searchGrade) {
            return byname && bygrade
        }
        // אם רק אחד מהם נכון 
        return byname || bygrade
    })

    let studentlis = filterfieldstudents.map((student,index) => { //אם נמצא מכניס אותו למערך עם הנתונים שלו 
        return(<Student
        key = {index}
        Fname = {student.Fname}
        Lname = {student.Lname}
        Grade = {student.Grade}
        
        
        />)
    })



    return (
        <>
        <label>Search for student: </label>
            <input type="text"
            onChange={(e) => setSearchName(e.target.value) }
            />
            <label>   Search by Grade: </label>
            <input type="number" 
            step="10" 
            onChange={(e) => setSearchGrade(e.target.value)}
            />
             {/* //הצגת המערך אחרי הסינון  */}
             {studentlis} 
        </>
    )

}