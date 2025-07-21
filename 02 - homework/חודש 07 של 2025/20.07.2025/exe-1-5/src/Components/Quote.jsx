import { useState, useEffect } from "react";

export function Quote() {
    const [quotes, setQuotes] = useState([
        { id: 1, text: "The greatest glory in living lies not in never falling, but in rising every time we fall.", author: "Nelson Mandela" },
        { id: 2, text: "The way to get started is to quit talking and begin doing.", author: "Walt Disney" },
        { id: 3, text: "Life is what happens when you're busy making other plans.", author: "John Lennon" },
        { id: 4, text: "The future belongs to those who believe in the beauty of their dreams.", author: "Eleanor Roosevelt" },
        { id: 5, text: "It is during our darkest moments that we must focus to see the light.", author: "Aristotle" }
    ]);
    const [show, setShow] = useState("")
    function quote(){
        let randomIndex = Math.floor(Math.random()*quotes.length)
        setShow(quotes[randomIndex])
    }
    useEffect(() => {
        quote()
    const randomQuotes = setInterval(() => {
        quote()
    }, 5000);
    return () => clearInterval(randomQuotes)
    }, []);

    return (
        <div>
            <p1>"{show.text}"</p1>
            <p>- {show.author}</p>
        </div>
        
    );
}