// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, sendPasswordResetEmail } from "firebase/auth";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCMvFelPHZembUJgNOr28uf7iDbMO393c4",
  authDomain: "practic-firebase-b6ab4.firebaseapp.com",
  projectId: "practic-firebase-b6ab4",
  storageBucket: "practic-firebase-b6ab4.firebasestorage.app",
  messagingSenderId: "929075652037",
  appId: "1:929075652037:web:1e961e8ea3133672e097ac"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);


export const register = async (email, password) => {
  const userCredential = await createUserWithEmailAndPassword(auth, email, password)
  if (!userCredential) {
    throw new Error ("cant register")
  }
  return userCredential
}

export const login = async (email,password) => {
  const userCredential = await signInWithEmailAndPassword(auth, email, password) // auth כדי שיקלוט מהדאטא בייס שלנו ולא משל מישהוא אחר 
  if (!userCredential) {
    throw new Error ("no such user")
  }
  return userCredential
}

 export const forgetpassword = async (email) =>{
  const emailCredential = await sendPasswordResetEmail(auth, email)
  if (!emailCredential){
    throw new Error("no such email here")
  }
  return emailCredential
}