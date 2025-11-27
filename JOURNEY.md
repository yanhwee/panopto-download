# Development Journey: Panopto Downloader

This document chronicles the research and development process of building a Panopto Video Downloader. It highlights the trade-offs between different technical approaches, from Python automation to pure client-side extensions.

## Objective
Create a reliable tool for students to download Panopto lectures, which often consist of dual video streams (Lecturer Camera + Presentation Slides).

---

## Phase 1: The Python Automation (Selenium + yt-dlp)
**"The Heavy Hitter"**

Our first approach was to use industry-standard tools for web scraping and video downloading.

*   **Architecture**:
    *   **Selenium**: Automates a real Chrome browser to handle the complex Single Sign-On (SSO) authentication.
    *   **Cookie Extraction**: Once logged in, the script extracts the session cookies.
    *   **yt-dlp**: These cookies are passed to `yt-dlp`, a powerful command-line media downloader, to handle the HLS streams.
*   **Outcome**: ✅ **Success**
    *   It works reliably.
    *   It handles the "Camera" vs "Slides" issue by letting `yt-dlp` parse the manifest.
*   **Trade-off**: High barrier to entry. Users must install Python, manage `pip` dependencies, and be comfortable using a Terminal.

---

## Phase 2: The Pure JavaScript Extension (HLS + mux.js)
**"The User-Friendly Ideal"**

To lower the barrier to entry, we attempted to build a "Pure JavaScript" Chrome Extension. The goal was a simple "Download" button injected directly into the page, with no Python required.

*   **Architecture**:
    *   **Network Sniffing**: The extension listens to `chrome.webRequest` to detect `.m3u8` playlist URLs.
    *   **Client-Side Downloading**: We implemented a custom downloader in `background.js` to fetch hundreds of `.ts` video segments.
    *   **Transmuxing**: We used the `mux.js` library to stitch these MPEG-TS segments into a single MP4 container directly in the browser memory.
*   **Challenges**:
    *   **Performance**: Downloading 20+ segments in parallel choked the network.
    *   **Memory Usage**: Storing a 2-hour lecture in browser RAM (Blob) is risky and can crash the tab.
    *   **Complexity**: Panopto serves "Master" playlists (menus) and "Variant" playlists (video). Distinguishing them programmatically was error-prone, leading to 0-byte downloads.
*   **Outcome**: ⚠️ **Partial Failure**. While technically impressive, it was too unstable for large files and complex network conditions.

---

## Phase 3: The "Lite" Extension (MP4 Sniffing)
**"The Shortcut"**

We observed that Panopto sometimes serves direct `.mp4` files for compatibility. We pivoted the extension to look exclusively for these.

*   **Architecture**:
    *   Simplified the extension to ignore HLS streams.
    *   Only detect `Content-Type: video/mp4` or `.mp4` URLs.
    *   Trigger Chrome's native download manager.
*   **Outcome**: ⚡ **Fast but Inconsistent**.
    *   When it works, it's instant.
    *   **Fatal Flaw**: Panopto does not *always* serve MP4s. Many videos are HLS-only, rendering this extension useless for those cases.

---

## Phase 4: The Reality Check (Native Messaging)
**"The Deployment Nightmare"**

We implemented the Native Messaging bridge. It worked in theory, but in practice:
*   **Installation Friction**: Users had to run a shell script, find their Extension ID, and edit a JSON file. This is too much for an average user.
*   **Fragility**: The "handshake" between Chrome and Python is extremely sensitive. Any stray print statement, path issue, or environment mismatch causes the connection to drop silently.

## Final Conclusion
After exploring all options, we have determined that **there is no "Magic Bullet"**.

1.  **Pure Extension**: Cannot handle the complexity of Panopto's streams.
2.  **Native Messaging**: Too hard to install and debug.
3.  **Pure Python**: The only reliable, robust solution.

**Recommendation**:
We will package the **Python Script** (Phase 1) as the final deliverable. It is honest, reliable, and does exactly what it says on the tin.
