importScripts(
  'https://www.gstatic.com/firebasejs/10.14.1/firebase-app-compat.js'
);

importScripts(
  'https://www.gstatic.com/firebasejs/10.14.1/firebase-messaging-compat.js'
);

const firebaseConfig = {
  apiKey: "AIzaSyBzxLIAJgEPS1go8gvOHGH5ZobzuHOE_58",
  authDomain: "cis-sermaize-connect.firebaseapp.com",
  projectId: "cis-sermaize-connect",
  storageBucket: "cis-sermaize-connect.firebasestorage.app",
  messagingSenderId: "1065319931797",
  appId: "1:1065319931797:web:5b4644a2bbcf255a38e09c"
};

firebase.initializeApp(firebaseConfig);

const messaging = firebase.messaging();

self.addEventListener('install', function(event) {
  self.skipWaiting();
});

self.addEventListener('activate', function(event) {
  event.waitUntil(self.clients.claim());
});

messaging.onBackgroundMessage(function(payload) {
  console.log(
    'CIS SERMAIZE - Background message received',
    payload
  );
});
self.addEventListener(
  'notificationclick',
  function(event) {

    event.notification.close();

    const urlCIS =
      'https://script.google.com/macros/s/AKfycbzClJ-siED0JMrCguhbt8VZs-zuBIQb19f_KeYSwee-bWweA8BAI47d92W5eLGZ96dvkA/exec';

    event.waitUntil(
      clients.openWindow(urlCIS)
    );
  }
);