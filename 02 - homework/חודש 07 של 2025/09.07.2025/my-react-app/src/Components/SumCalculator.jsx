import { useState } from "react"

export function SumCalculator(props){
    const [number1, setNumber1] = useState()
    const [number2, setNumber2] = useState()
    const [result, setResult] =useState()

    function sum_n1_and_n2(){
        if (/^-?\d+(\.\d+)?$/.test(number1) && /^-?\d+(\.\d+)?$/.test(number2)){
            setResult(number1+number2)
        }else{
            setResult("enter only numbers")
        }
    }
    return(
        <>
        <h1>Sum Calculator</h1>
        <input type="text"
        onChange={(e) => setNumber1(+e.target.value)}
        />

        <input type="text"
        onChange={(e) => setNumber2(+e.target.value)}
        />

        <button onClick={sum_n1_and_n2}>{props.buttonText}</button>
        <br />
        <p1>result: {result}</p1>
        <br /><br />
        </>
    )
}