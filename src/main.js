import { createApp } from 'vue'
import App from './App.vue'  //app is imported from App.vue

createApp(App).mount('#app') //this is what is sent to index.html


// Import the functions you need from the SDKs you need
import firebase from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import 'firebase/storage';

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
//const firebaseConfig = {
//    apiKey: "AIzaSyCsVPwC-0RXoEgFQR8_M_Ron3F1--YrnKo",
//    authDomain: "freetimefun-5a139.firebaseapp.com",
//    projectId: "freetimefun-5a139",
//    databaseURL: "https://freetimefun-5a139.firebaseio.com",
//    storageBucket: "freetimefun-5a139.appspot.com",
//    messagingSenderId: "325207380330",
//    appId: "1:325207380330:web:01ed8b306d52dd29579513",
//    measurementId: "G-F1Q2HJNH12"
// };


//firebase.initializeApp(firebaseConfig)




//Passing data from javscript to python and back again

//const spawner = require('child_process').spawn;  //defining the spawner

//const data_to_pass_in = 'Send til to python script';  

//console.log('Send til to python script')

//const python_process = spawner('python', ['./python.py', data_to_pass_in])   //passing the "data_to_pass_In to the python file at the described url, and in language 'python'"

//python_process.stdout.on('data', (data) => {
 // console.log(data.toString());
//})