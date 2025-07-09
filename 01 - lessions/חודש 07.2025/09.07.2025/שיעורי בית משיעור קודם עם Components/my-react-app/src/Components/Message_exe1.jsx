import React, { useState } from "react";

export function Message() {//לשים לב שכאן האקספורט הוא בהתחלה 
    //1. properties
    const [message, setMessage] = useState("Hello");

    //2. functions
    function toggleMessage() {
        if (message === "Hello") {
            setMessage("GoodBye");
        } else {
            setMessage("Hello");
        }
    }

    //3. html + js
    return (
        <div>
            <button onClick={toggleMessage}>toggle</button>
            <p>{message}</p>
        </div>
    );
}