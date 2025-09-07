// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut, onAuthStateChanged } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {

};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app); // יוצר אובייקט Authentication של Firebase - זה המנגנון שמטפל בכל פעולות הזיהוי והאימות במערכת כמו רישום משתמשים חדשים, כניסה למערכת, יציאה, ניהול סיסמאות ועוד

export async function registerUser(email, password) {
    try {
      return await createUserWithEmailAndPassword(auth, email, password);
        
    } catch (error) {
        console.error(error);
        throw error;
    }
}

export async function loginUser(email, password) {
    try {
        return await signInWithEmailAndPassword(auth, email, password);
    } catch (error) {
        console.error(error);
        throw error;
    }
}

export async function logoutUser() {
    try {
        await signOut(auth);
    } catch (error) {
        console.error(error);
        throw error;
    }
}

export function onAuthChange(callback) {
    return onAuthStateChanged(auth, callback);
}