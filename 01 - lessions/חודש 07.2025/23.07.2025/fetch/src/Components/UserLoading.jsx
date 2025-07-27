import {useEffect, useState } from "react"

export function UserLoading(){

    const [info, setInfo] = useState([])//כללי מחוץ לסינק
    const [loading, setLoading] = useState(true)

    async function getUsers(){
        try{
            let response = await fetch ("https://jsonplaceholder.typicode.com/users")
            const data = await response.json()
            setInfo(data)
        }
        catch (Error){
            console.log("Error")
        }
        finally{
            setLoading(false)
        }}
        useEffect(()=>{
            setTimeout(getUsers,5000)
        },[])

        let mapinfo = info.map((userInfo, index) => {
            return( 
                <li key={index}>
                <p>Name: {userInfo.name}</p>
                <p>email: {userInfo.email}</p>
                <p>street: {userInfo.address.street}</p>
                <p>city: {userInfo.address.city}</p>
                <br /> <br />
                </li>
            )
        })
        if (loading) return <p>Loading....</p>

    return(
        <>
        <ul>{mapinfo}</ul>
        </>
    )
}