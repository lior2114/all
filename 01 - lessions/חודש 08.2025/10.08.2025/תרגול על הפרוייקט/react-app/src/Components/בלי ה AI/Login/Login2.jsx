import { login } from "../../api/api"
export function Login(){
const handlelogin = async () =>{
    try{
      let data = await login({
        user_email:"test@test.com",
        user_password: "test123"
      })
      console.log(data)
    }
    catch (error){
      console.log(error.message)
    }
  }

  
  return(
    <button onClick={handlelogin}>login</button>
)
}