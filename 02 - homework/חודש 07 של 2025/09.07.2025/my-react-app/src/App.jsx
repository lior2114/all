
import './App.css'
import { AgeChecker } from './Components/AgeChecker'
import { PasswordMatchChecker } from './Components/PasswordMatchChecker'
import { SumCalculator } from './Components/SumCalculator'
import { UserNameDisplay } from './Components/UserNameDisplay'

function App() {

  return (
    <>
        <UserNameDisplay emptyMessage = "Please enter your username"/>
        <SumCalculator buttonText = "click to sum"/>
        <AgeChecker
         buttonText ="בדוק"
         minorMessage = "קטין"
         adultMessage = "בוגר"
         errorMessage= "הכנס מספר תקין"
        />
        <PasswordMatchChecker 
        buttonText = "לחץ כדי לבדוק אם הסיסמאות תואמות"
        matchMessage = "הסיסמאות תואמות"
        notMatchMessage = "הסיסמאות לא תואמות"
        errorMessage= "סיסמא קצרה מידי / ריקה"
        />
    </>
  )
}

export default App
