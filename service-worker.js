const CACHE_NAME = 'cis-sermaize-v1';

self.addEventListener('install', function(event) {
  console.log('CIS SERMAIZE - Service Worker installé');
  self.skipWaiting();
});

self.addEventListener('activate', function(event) {
  console.log('CIS SERMAIZE - Service Worker actif');
  event.waitUntil(self.clients.claim());
});
