import { Link } from 'react-router-dom';

export default function NavBar() {
    return (
        <nav>
            <Link to="/">Home</Link> |
            <Link to="/tasks">Tasks</Link> |
            <Link to="/addtask">Add Task</Link>
        </nav>
    );
}