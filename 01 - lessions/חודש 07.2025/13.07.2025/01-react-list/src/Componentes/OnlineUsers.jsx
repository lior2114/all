export function OnlineUsers(){
    let users = [
        {username : "Lior", isOnline : true},
        {username : "Dana", isOnline : false},
        {username : "Amit", isOnline : true},
        {username : "Noa", isOnline : false}
    ]

    let filterandmapUsers = users
    .filter((online) => (online.isOnline))
    .map((show,index)=><li key = {index}>{show.username}🟢</li>)


    return (
        <>
            <h1>Exe 9 - OnlineUsers</h1>
            <div>{filterandmapUsers}</div>
        </>
    )
}