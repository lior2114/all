import { useState, useEffect } from 'react';

function Counter() {
    const [count, setCount] = useState(0);


    useEffect(() => {

        console.log("המשתנה count השתנה:", count);
    }, [count]); // ה־effect ירוץ בכל פעם ש־count משתנה

    return (
        <div>
            <h1>Counter: {count}</h1>
            <button onClick={() => setCount(count + 1)}>+</button>
        </div>
    );
}
export default Counter;
