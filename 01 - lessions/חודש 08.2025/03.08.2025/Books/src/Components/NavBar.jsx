import { Link } from 'react-router-dom';

export function NavBar(){

    return(
        <div>
            <Link to ="/">Home</Link><br />
            <Link to = "/Books">Books</Link><br />
            <Link to = "AddBooks">Add Books</Link>
        </div>
    )
}