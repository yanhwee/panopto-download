# Panopto Video Downloader Walkthrough

I have created a custom tool to help you download Panopto videos. This tool uses a real browser window to let you log in to your university's portal, ensuring you can access the videos you have permission to view.

## Prerequisites
- **Google Chrome** must be installed on your Mac.

## How to Use

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

## Troubleshooting
- **Browser closes too fast?** Make sure you press Enter in the terminal *only after* the video page has fully loaded.
- **Download fails?** Ensure you have played the video for a second in the browser to ensure the session is active.
