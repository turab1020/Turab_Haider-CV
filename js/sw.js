// Service Worker — lightweight caching for offline support
// Videos are NOT pre-cached (too large); they cache on first play.

const CACHE_NAME = 'cv-portfolio-v2';

// Only cache small, critical assets on install
const CRITICAL_ASSETS = [
    './',
    './index.html',
    './css/style.css',
    './js/main.js',
    './images/profile.jpg'
];

// Cache critical shell on install
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => cache.addAll(CRITICAL_ASSETS))
            .then(() => self.skipWaiting())
            .catch((err) => console.log('SW: Cache failed', err))
    );
});

// Clean up old caches on activate
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys()
            .then((names) => Promise.all(
                names.filter(n => n !== CACHE_NAME).map(n => caches.delete(n))
            ))
            .then(() => self.clients.claim())
    );
});

// Fetch strategy:
//  - HTML/CSS/JS: stale-while-revalidate (fast + fresh)
//  - Videos: cache-first (they're large, avoid re-downloading)
//  - External: network-only (fonts, icons from CDN)
self.addEventListener('fetch', (event) => {
    if (event.request.method !== 'GET') return;

    const url = new URL(event.request.url);

    // Skip external requests — let the browser handle them normally
    if (url.origin !== self.location.origin) return;

    // Video files: cache-first (large, rarely change)
    if (url.pathname.endsWith('.mp4')) {
        event.respondWith(
            caches.match(event.request).then((cached) => {
                if (cached) return cached;
                return fetch(event.request).then((response) => {
                    if (response && response.status === 200) {
                        const clone = response.clone();
                        caches.open(CACHE_NAME).then(c => c.put(event.request, clone));
                    }
                    return response;
                });
            })
        );
        return;
    }

    // Everything else: stale-while-revalidate
    event.respondWith(
        caches.match(event.request).then((cached) => {
            const fetchPromise = fetch(event.request)
                .then((response) => {
                    if (response && response.status === 200) {
                        const clone = response.clone();
                        caches.open(CACHE_NAME).then(c => c.put(event.request, clone));
                    }
                    return response;
                })
                .catch(() => cached);

            return cached || fetchPromise;
        })
    );
});
