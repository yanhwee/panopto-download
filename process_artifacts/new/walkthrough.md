# Panopto Video Downloader Walkthrough

I have created a custom tool to help you download Panopto videos. This tool uses a real browser window to let you log in to your university's portal, ensuring you can access the videos you have permission to view.

## Prerequisites
- **Google Chrome** must be installed on your Mac.

## How to Use
## Option 1: Python Downloader (Robust)

1.  **Open Terminal** and navigate to the project folder:
    ```bash
    cd /Users/yanhwee/Documents/repos/panopto-download
    ```

2.  **Run the Downloader**:
    Execute the script using the virtual environment's Python:
    ```bash
    ./venv/bin/python3 panopto_downloader.py
    ```

3.  **Follow the Prompts**:
    - **Paste URL**: When asked, paste the full URL of the Panopto video you want to download.
    - **Log In**: A Chrome window will open. Log in to your school's portal as you normally would.
    - **Navigate**: Ensure the video page is loaded and you can see the player.
    - **Confirm**: Go back to the terminal and press **Enter** when the video is visible.

4.  **Download**:
    The script will extract the necessary cookies and download the video to the current folder.

## Option 2: Chrome Extension (Hybrid / Native Messaging)

This is the recommended method. It combines the ease of a browser button with the power of Python.

**Part 1: Install the Native Host (One-time setup)**
1.  Open Terminal in the project folder.
2.  Run the installer:
    ```bash
    ./install_host.sh
    ```

**Part 2: Install the Extension**
1.  Open Chrome and go to `chrome://extensions`.
2.  Enable **Developer mode** (top right).
3.  Click **Load unpacked**.
4.  **IMPORTANT**: Select the `extension_pure` folder (NOT the `extension` folder).

**Part 3: Link Them**
1.  Copy the **ID** of the extension you just installed (e.g., `abcdef...`).
2.  Open the file: `~/Library/Application Support/Google/Chrome/NativeMessagingHosts/com.yanhwee.panopto_downloader.json`
3.  Replace `REPLACE_WITH_EXTENSION_ID` with your actual ID.
    *   Example: `"chrome-extension://abcdefghijklmnop.../"`
4.  **Restart Chrome** (fully quit and reopen).

**Usage**:
1.  Go to a Panopto video.
2.  Click the extension icon.
3.  Click **Download**.
4.  The video will be downloaded silently to your project folder (or Downloads).

## Verification Results

### 1. Basic Download
- **Test**: Run `python3 panopto_downloader.py` and paste a URL.
- **Result**: ✅ Browser opens, login works, and video downloads.

### 2. Batch Download
- **Test**: Create `urls.txt` with multiple links and run `python3 panopto_downloader.py urls.txt`.
- **Result**: ✅ Script logs in once and downloads all videos sequentially.

### 3. CLI Arguments
- **Test**: Run `python3 panopto_downloader.py "https://..."`.
- **Result**: ✅ Script skips the prompt and starts immediately.

### 4. File Organization
- **Test**: Download a video.
- **Result**: ✅ Video is saved inside the `videos/` folder.

## Troubleshooting
- **Browser closes too fast?** Make sure you press Enter in the terminal *only after* the video page has fully loaded.
- **Download fails?** Ensure you have played the video for a second in the browser to ensure the session is active.
