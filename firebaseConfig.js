// firebaseConfig.js
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCz2rnWXzzCmnSbl4hTM32EegHtYGZSO0I",
  authDomain: "attendence-system-b6eb9.firebaseapp.com",
  projectId: "attendence-system-b6eb9",
  storageBucket: "attendence-system-b6eb9.firebasestorage.app",
  messagingSenderId: "901629340513",
  appId: "1:901629340513:web:05d059e98bc51c360d7320",
  measurementId: "G-B4NKRXFWLD",
  databaseURL: "https://attendence-system-b6eb9-default-rtdb.firebaseio.com/"
};


// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const database = firebase.database();
