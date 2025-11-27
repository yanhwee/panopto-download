# Implementation Plan - Phase 3: Native Messaging (Hybrid)

## Goal
Integrate the Chrome Extension with a local Python script using Native Messaging. This allows the extension to detect videos and handle authentication, while offloading the heavy downloading and merging tasks to `yt-dlp` running on the host machine.

## User Review Required
> [!IMPORTANT]
> **Installation Complexity**: This approach requires running a one-time install script (`install_host.sh`) on your machine to register the Python script with Chrome. This is a security requirement for Native Messaging.

## Proposed Changes

### 1. Host Configuration (Python Side)
We need to finalize the Python script that listens for messages from Chrome.
#### [MODIFY] [panopto_host.py](../host/panopto_host.py)
- Update to receive JSON messages `{ "url": "...", "cookies": "..." }`.
- Invoke `yt-dlp` with the provided cookies and URL.
- Send progress/status updates back to Chrome (optional, but good for UX).

#### [MODIFY] [install_host.sh](../install_host.sh)
- Ensure it correctly writes the `com.panopto.downloader.json` manifest to the Chrome NativeMessagingHosts directory.
- Verify paths are absolute (Chrome requirement).

### 2. Extension Configuration (Chrome Side)
#### [MODIFY] [manifest.json](../extension_pure/manifest.json)
- Add `"permissions": ["nativeMessaging"]`.

#### [MODIFY] [background.js](../extension_pure/background.js)
- Replace the current download logic with `chrome.runtime.sendNativeMessage`.
- Handle the response from the Python script.

#### [MODIFY] [popup.js](../extension_pure/popup.js)
- Update UI to indicate "Sent to Downloader" instead of showing a progress bar (since the download happens outside the browser).

## Verification Plan
1.  Run `install_host.sh`.
2.  Reload the extension.
3.  Navigate to a Panopto video.
4.  Click "Download".
5.  Verify that a Python process starts and `yt-dlp` begins downloading the video to the local disk.
