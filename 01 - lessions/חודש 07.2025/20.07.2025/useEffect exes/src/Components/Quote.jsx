import { useState, useEffect } from "react";

export function Quote() {
    const [quotes, setQuotes] = useState([
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The way to get started is to quit talking and begin doing. - Walt Disney",
        "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
        "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt",
        "If you look at what you have in life, you'll always have more. - Oprah Winfrey"
    ]);
    
    const [currentQuote, setCurrentQuote] = useState("");
    
    const getRandomQuote = () => {
        const randomIndex = Math.floor(Math.random() * quotes.length);
        setCurrentQuote(quotes[randomIndex]);
    };
    
    useEffect(() => {
        getRandomQuote(); // ציטוט ראשוני
        const timer = setInterval(getRandomQuote, 5000); // כל 5 שניות
        return () => clearInterval(timer);
    }, []);

    return (
        <div>{currentQuote}</div>
    );
}