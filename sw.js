// Offline-Cache für GitHub Pages
const C="flipcheck-v2";
const FILES=["./","index.html","manifest.webmanifest","icon-180.png","icon-192.png","icon-512.png","icon.svg","favicon.ico","favicon.svg","favicon-32.png","favicon-16.png"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(FILES)));self.skipWaiting();});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==C).map(k=>caches.delete(k)))));self.clients.claim();});
// Netzwerk zuerst (damit Updates ankommen), offline aus dem Cache
self.addEventListener("fetch",e=>{ if(e.request.method!=="GET") return;
  e.respondWith(fetch(e.request).then(r=>{ const cp=r.clone(); caches.open(C).then(c=>c.put(e.request,cp)); return r; }).catch(()=>caches.match(e.request,{ignoreSearch:true}).then(r=>r||caches.match("index.html"))));
});
