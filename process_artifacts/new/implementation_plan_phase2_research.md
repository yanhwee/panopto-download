# Phase 2: Pure Client-Side Chrome Extension (Research)

## Goal
Create a standalone Chrome Extension that downloads and merges Panopto videos entirely within the browser, removing the need for Python or external installation scripts.

## Architecture: Pure JavaScript
Instead of Native Messaging, we will use **Service Workers** and **WebAssembly**.
1.  **M3U8 Detection**: The extension listens for network requests to find the `.m3u8` playlist.
2.  **Segment Downloading**: The extension fetches all `.ts` video segments directly.
3.  **Merging**:
    - **Option A (Simpler)**: Use `mux.js` to transmux MPEG-TS segments into MP4 on the fly.
    - **Option B (Robust)**: Use `ffmpeg.wasm` to merge segments. This is heavier but supports more formats.
4.  **Download**: The final blob is saved to the user's computer using the `chrome.downloads` API.

## Trade-offs vs. Python Approach
| Feature | Python (Native Messaging) | Pure JavaScript (Extension) |
| :--- | :--- | :--- |
| **Setup** | Complex (Requires install script) | Easy (Just install extension) |
| **Performance** | Fast (Native code) | Slower (Browser limits) |
| **Reliability** | High (`yt-dlp` is battle-tested) | Medium (Custom implementation) |
| **Memory** | Low impact on browser | High impact (Large videos may crash) |

## Proposed Changes (If we proceed)

### Chrome Extension Structure
#### [NEW] [manifest.json](../extension/manifest.json)
- Permissions: `webRequest`, `webRequestBlocking`, `downloads`, `offscreen` (for ffmpeg.wasm).

#### [NEW] [background.js](../extension/background.js)
- Intercepts `.m3u8` requests.
- Manages the download queue.

#### [NEW] [offscreen.js](../extension/offscreen.js)
- Runs `ffmpeg.wasm` or `mux.js` to merge files (since Service Workers can't easily handle heavy processing or DOM access).

## Conclusion
This approach is **feasible** and offers a better user experience (no setup), but is significantly **more complex to implement** than the Python wrapper. It requires handling binary data streams, memory management, and potential browser restrictions on large blobs.
