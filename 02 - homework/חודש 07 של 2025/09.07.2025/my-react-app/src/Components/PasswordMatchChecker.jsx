import { useState } from "react"

export function PasswordMatchChecker(props){
    
    const [Password, setPassword] = useState()
    const [returnPassword, setReturn_Password] = useState()
    const[checking,SetChecking] = useState()


    function hasLeadingOrTrailingSpaces(str) {
        return str !== str.trim();
    }
    function check_match_passwords(){
        if (!Password || Password.trim().length < 4){
            SetChecking(props.errorMessage)
        }
        else if (hasLeadingOrTrailingSpaces(Password) || hasLeadingOrTrailingSpaces(returnPassword)){
            SetChecking("בסיסמא שלך יש רווחים תמחק אותם")
        }
        else if (Password.trim() === returnPassword.trim()){
            SetChecking(props.matchMessage)
        }else{
            SetChecking(props.notMatchMessage)
        }
    }
    return(
        <>
        <h1>PasswordMatchChecker</h1>
        <label>Password: </label>
            <input type="text"
            onChange={(e)=> setPassword(e.target.value)}
            />
            <br /><br />
            <label>Type Password again: </label>
            <input type="text"
            onChange={(e)=> setReturn_Password(e.target.value) }
            />
            <br /><br />
            <button onClick={check_match_passwords}>{props.buttonText}</button>
            <div>{checking}</div>
        </>
    )
}