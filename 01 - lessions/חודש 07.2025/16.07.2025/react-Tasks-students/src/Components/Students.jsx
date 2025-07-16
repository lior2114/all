import { useState } from "react"
import { Student } from "./student"
export function Students(props){
    const [search , setSearch] = useState("")
    const filteredStudents = props.students.filter((student) =>{
        let fullName = student.Fname + " " + student.Lname
        return fullName.toLowerCase().includes(search.toLowerCase())
    })

    //אחרי הפילטר יחזיר לתוך משתנה מאפ מה שזה מצא ויציג אותו על הדף 
    let studentClass = filteredStudents.map((student,index) =>{
       return (<Student
        key = {index}
        Fname = {student.Fname}
        Lname = {student.Lname}
        Grade = {student.Grade}
        />)})

    return(
        <>
        <input type="text" placeholder="search..." onChange={(e) => setSearch(e.target.value)}></input>
            {studentClass}
        </>
    )
}