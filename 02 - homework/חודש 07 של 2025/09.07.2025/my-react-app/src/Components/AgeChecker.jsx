import { useState } from "react"

export function AgeChecker(props){
    const [text_age, setText_age] = useState()
    const [check_age, setCheck_age] = useState()

    function checking_age(){
        if (/^-?\d+(\.\d+)?$/.test(text_age)) {
            const age = text_age;

            if (age > 0 && age < 18) {
                setCheck_age(props.minorMessage);
            } else if (age >= 18 && age <= 120) {
                setCheck_age(props.adultMessage);
            }else if (age > 120){
                setCheck_age(props.errorMessage)
            }
        } else {
            setCheck_age(props.errorMessage) // טיפול בשגיאה אם לא מספר בכלל
            }
        }

    return(
        <>
        <h1>AgeChecker</h1>
        <input type="text"
        onChange={(e)=>setText_age(+e.target.value)}
        />
        <button onClick={checking_age}>{props.buttonText}</button>
        <div>{check_age}</div>
        </>
    )
}