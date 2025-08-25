import { initializeApp } from "https://esm.run/firebase/app";
import { getAnalytics } from "https://esm.run/firebase/analytics";
import { GoogleAuthProvider } from "https://esm.run/firebase/auth/web-extension";
import { config } from "dotenv";

config();
const firebaseConfig = {
    apiKey: process.env.FIREBASE_API_KEY,
    authDomain: process.env.FIREBASE_AUTH_DOMAIN,
    projectId: process.env.FIREBASE_PROJECT_ID,
    storageBucket: process.env.FIREBASE_STORAGE_BUCKET,
    messagingSenderId: process.env.FIREBASE_MESSAGING_SENDER_ID,
    appId: process.env.FIREBASE_APP_ID,
    measurementId: process.env.FIREBASE_MEASUREMENT_ID
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

const loginButton = document.getElementById("Login button");
const auth = getAuth();

loginButton.addEventListener("click", () => {
    signInWithPopup(auth, new GoogleAuthProvider());
});