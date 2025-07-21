import { useState, useEffect } from 'react';

function Counter() {
    const [count, setCount] = useState(0);
    useEffect(() => {
        console.log("התחלתי count מהתחלה:", count);
    }, [count]); // משתנה count מתעדכן בכל פעם ש-effect

    return (
        <div>
            <h1>Counter: {count}</h1>
            <button onClick={() => setCount(count + 1)}>+</button>
        </div>
    );
}

export default Counter;