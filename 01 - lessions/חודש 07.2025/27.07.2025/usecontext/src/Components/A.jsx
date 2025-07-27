import { useContext } from 'react';
import CounterContext from '../Contexts/CounterContext';

export function A() {
    const { count, setCount} = useContext(CounterContext);
    
    return (
        <div>
            <h2>A Component</h2>
            <div>Count from context: {count}</div>
            <br />
            <button onClick={() => setCount(count + 1)}>
                לחץ
            </button>
        </div>
    );
}