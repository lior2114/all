import { useEffect, useState } from "react"

export function PostList(){
    const [posts, setPosts] = useState([])
    const [loading, setLoading] = useState(true)

    async function getPosts(){
        try{
            let response = await fetch("https://jsonplaceholder.typicode.com/posts"); // await מחכה עד שיגיעו הנתונים ואז יציג
            const data = await response.json();// await מחכה עד שיחלץ את המידע לקובץ גייסון
            setPosts(data)
        }
        catch (Error){
            console.log("Error",Error)
        }
        finally{
            setLoading(false)
        }
    }
    useEffect(()=>{
        getPosts()
    }, [])

    let mapPost = posts.map((post, index) => {
        return(
            <li key={index} style={{padding:"10px", margin:"10px", border:"10px", color: "red"}}>
                <h2>{post.title}</h2>
                <p>{post.body}</p>
            </li>
        )
    })

    if (loading) return <p>Loading...</p>

    return(
        <>
            <h1>Hello Fetch</h1>    
            <ul>{mapPost}</ul>
            
        </>
    )
}