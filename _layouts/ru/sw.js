"use strict";

/**
 * Class to handle service worker caching and request serving.
 * @param {string} offlinePage - The URL of the page to show when offline.
 * @param {boolean} debugMode - If true, debug information will be logged to the console.
 */
class ServiceWorkerManager {
  /**
   * Constructor for the ServiceWorkerManager class.
   * @param {string} offlinePage - The URL of the page to show when offline.
   * @param {boolean} debugMode - If true, debug information will be logged to the console.
   */
  constructor(offlinePage, debugMode) {
    /**
     * Version of the cache used for cache management.
     */
    this.CACHE_VERSION = "v3";

    /**
     * Array of cache keys that the service worker should care about, used to keep track and delete old caches.
     */
    this.CACHE_KEYS = [this.CACHE_VERSION];

    /**
     * The URL of the page to show when offline.
     */
    this.offlinePage = offlinePage;

    /**
     * A boolean indicating if debug information should be logged to the console.
     */
    this.debugMode = debugMode;

    /**
     * Initialize the service worker by setting up the event listeners.
     */
    this.init();
  }

  /**
   * Initialize the service worker by setting up event listeners for install, activate, fetch and message events.
   */
  init() {
    self.addEventListener("install", this.onInstall.bind(this));
    self.addEventListener("activate", this.onActivate.bind(this));
    self.addEventListener("fetch", this.onFetch.bind(this));
    self.addEventListener("message", this.onMessage.bind(this));
  }

  /**
   * Logs a message to the console if debug mode is enabled.
   * @param {any} message - The message to log.
   */
  debug(message) {
    if (this.debugMode) {
      console.log(message);
    }
  }

  /**
   * Event handler for the install event.
   * Caches the offline page and forces the waiting service worker to become the active service worker.
   * @param {InstallEvent} event - The install event.
   */
  onInstall(event) {
    this.debug("Installing Service Worker");
    event.waitUntil(
      this.cacheOfflinePage()
        .then(() => self.skipWaiting())
        .catch((error) => {
          this.debug(`Install event error: ${error}`);
        })
    );
  }

  /**
   * Event handler for the activate event.
   * Clears old caches and takes control of all clients.
   * @param {ExtendableEvent} event - The activate event.
   */
  onActivate(event) {
    this.debug("Activating Service Worker");
    event.waitUntil(
      this.clearOldCaches()
        .then(() => self.clients.claim())
        .catch((error) => {
          this.debug(`Activate event error: ${error}`);
        })
    );
  }

  /**
   * Event handler for the fetch event.
   * Serves requests from the cache if possible, otherwise fetches from the network.
   * Caches successful network responses.
   * @param {FetchEvent} event - The fetch event.
   */
  onFetch(event) {
    if (event.request.method !== "GET") return;

    const requestUrl = new URL(event.request.url);
    if (requestUrl.origin !== self.location.origin) return;

    const isManifestOrIcon =
      requestUrl.pathname.endsWith("/manifest.json") ||
      requestUrl.pathname.endsWith("/icon-192.png") ||
      requestUrl.pathname.endsWith("/icon-512.png");

    if (isManifestOrIcon) {
      event.respondWith(
        fetch(event.request)
          .then((networkResponse) => {
            if (
              networkResponse &&
              networkResponse.status === 200 &&
              networkResponse.type === "basic"
            ) {
              const responseClone = networkResponse.clone();
              caches
                .open(this.CACHE_VERSION)
                .then((cache) => cache.put(event.request, responseClone))
                .catch((error) =>
                  this.debug(`Cache write failed for ${event.request.url}: ${error}`)
                );
            }
            return networkResponse;
          })
          .catch(() =>
            caches.match(event.request).then(
              (cachedResponse) =>
                cachedResponse ||
                new Response("", {
                  status: 503,
                  statusText: "Service Unavailable",
                })
            )
          )
      );
      return;
    }

    if (event.request.mode === "navigate") {
      event.respondWith(
        fetch(event.request).catch((error) =>
          this.handleFetchError(event.request, error)
        )
      );
      return;
    }

    event.respondWith(
      caches.match(event.request).then((cachedResponse) => {
        if (cachedResponse) return cachedResponse;

        return fetch(event.request)
          .then((networkResponse) => {
            if (
              networkResponse &&
              networkResponse.status === 200 &&
              networkResponse.type === "basic"
            ) {
              const responseClone = networkResponse.clone();
              caches
                .open(this.CACHE_VERSION)
                .then((cache) => cache.put(event.request, responseClone))
                .catch((error) =>
                  this.debug(`Cache write failed for ${event.request.url}: ${error}`)
                );
            }
            return networkResponse;
          })
          .catch((error) => this.handleFetchError(event.request, error));
      })
    );
  }

  /**
   * Event handler for the message event.
   * Listens for a 'skipWaiting' message to call self.skipWaiting().
   * @param {MessageEvent} event - The message event.
   */
  onMessage(event) {
    if (event.data.action === "skipWaiting") {
      self.skipWaiting();
    }
  }

  /**
   * Handle fetch errors, such as failing to retrieve a resource from the cache or network.
   * For navigation requests, an offline page is shown.
   * For image requests, an offline image is shown.
   * @param {Request} request - The failed request.
   * @param {Error} error - The error that caused the fetch to fail.
   */
  handleFetchError(request, error) {
    this.debug(`Fetch error for ${request.url}: ${error}`);

    if (request.mode === "navigate") {
      return caches.match(this.offlinePage).then((offlineResponse) => {
        if (offlineResponse) return offlineResponse;
        return new Response("Offline", {
          status: 503,
          statusText: "Service Unavailable",
          headers: { "Content-Type": "text/plain; charset=utf-8" },
        });
      });
    }

    return new Response("", { status: 503, statusText: "Service Unavailable" });
  }

  /**
   * Caches the offline page.
   * @returns {Promise} - A promise that resolves once the offline page is cached.
   */
  cacheOfflinePage() {
    this.debug("Cache offline page");
    return caches
      .open(this.CACHE_VERSION)
      .then((cache) => cache.addAll([this.offlinePage]));
  }

  /**
   * Deletes all caches that do not match the current cache version.
   * @returns {Promise} - A promise that resolves once old caches are deleted.
   */
  clearOldCaches() {
    this.debug("Clean old caches");
    return caches
      .keys()
      .then((keys) =>
        Promise.all(
          keys
            .filter((key) => !this.CACHE_KEYS.includes(key))
            .map((key) => caches.delete(key))
        )
      );
  }
}

// Create an instance of the ServiceWorkerManager class.
new ServiceWorkerManager("/offline/index.html", false);
