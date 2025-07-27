async function getPosts() {
    try{
        let response = await fetch("https://jsonplaceholder.typicode.com/posts"); // await מחכה עד שיגיעו הנתונים ואז יציג
        const data = await response.json();// await מחכה עד שיחלץ את המידע לקובץ גייסון
        console.log(data);
    }
    catch (Error){
        console.log("Error",Error)
        alert("error")
    }

}

getPosts();