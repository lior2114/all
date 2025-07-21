import { useState, useEffect } from 'react';

export function Clock() {
    const [time, setTime] = useState(new Date());

    useEffect(() => {
        console.log("A")
        const timer = setInterval(() => {
            setTime(new Date());
        }, 1000);

        return () => clearInterval(timer);
    }, []);

    return (
        <div>
            <h2>השעה כעת:</h2>
            <h1>{time.toLocaleTimeString()}</h1>
        </div>
    );
}

