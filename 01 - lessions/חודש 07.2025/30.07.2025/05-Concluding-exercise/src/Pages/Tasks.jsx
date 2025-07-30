import { useState } from "react"

export default function Tasks({ tasks }){
    
    return(
        <>
        <h2>Tasks</h2>
        {tasks.length === 0 ? (
            <p>No tasks available</p>
        ) : (
            <ol type="1">
                {tasks.map((task, index) => (
                    <li key={index}>{task}</li>
                ))}
            </ol>
        )}
        </>
    )
}