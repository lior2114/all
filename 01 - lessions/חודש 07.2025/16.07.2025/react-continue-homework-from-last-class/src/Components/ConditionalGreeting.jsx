import { useState } from "react";

export function ConditionalGreeting() {
    const [isMorning, setIsmorning] = useState(false);

    return (
        <h1 onClick={() => setIsmorning(!isMorning)}>
            {isMorning ? "Good morning!" : "Good evening!"}
        </h1>
    );
}