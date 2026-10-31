/**
 * SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
 * SPDX-License-Identifier: Apache-2.0 OR MIT
 * Zero-Telemetry Offline Service Worker — Bank Statement Parser
 */

'use strict';

var CACHE_NAME = 'bsp-docs-v0.0.8';
var OFFLINE_URL = '/offline/index.html';
var PRECACHE_URLS = [
  '/',
  '/index.html',
  OFFLINE_URL,
  '/getting-started/index.html',
  '/formats/index.html',
  '/architecture/index.html',
  '/benchmarks/index.html',
  '/faqs/index.html',
  '/manifest.json'
];

self.addEventListener('install', function (event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function (cache) {
      return cache.addAll(PRECACHE_URLS);
    }).then(function () {
      return self.skipWaiting();
    })
  );
});

self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(
        keys.map(function (key) {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
          return null;
        })
      );
    }).then(function () {
      return self.clients.claim();
    })
  );
});

self.addEventListener('fetch', function (event) {
  if (event.request.method !== 'GET') return;
  var url = new URL(event.request.url);
  if (url.origin !== self.location.origin) return;

  event.respondWith(
    fetch(event.request)
      .then(function (response) {
        if (response && response.status === 200 && response.type === 'basic') {
          var clone = response.clone();
          caches.open(CACHE_NAME).then(function (cache) {
            cache.put(event.request, clone);
          });
        }
        return response;
      })
      .catch(function () {
        return caches.match(event.request).then(function (cached) {
          if (cached) return cached;
          if (event.request.mode === 'navigate') {
            return caches.match(OFFLINE_URL);
          }
          return new Response('', { status: 503, statusText: 'Offline' });
        });
      })
  );
});
