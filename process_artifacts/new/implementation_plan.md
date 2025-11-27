# Panopto Video Downloader Plan

## Goal
Create a user-friendly Python tool to download Panopto videos. The tool will handle university SSO login via a browser (Selenium) and then use `yt-dlp` to download the video stream.

## User Review Required
> [!IMPORTANT]
> This tool requires **Google Chrome** to be installed on your machine, as it uses Selenium with the Chrome WebDriver.

## Proposed Changes

### Project Structure
I will create a new Python project in the current directory.

#### [NEW] [requirements.txt](../requirements.txt)
Dependencies:
- `yt-dlp`: For downloading the video stream.
- `selenium`: For browser automation and handling SSO login.
- `webdriver-manager`: To automatically manage the ChromeDriver binary.

#### [NEW] [panopto_downloader.py](../panopto_downloader.py)
A Python script that:
1.  Asks the user for the Panopto Video URL.
2.  Launches a Chrome browser window.
3.  Navigates to the URL and pauses to let the user log in (if required).
4.  Once the video page is loaded, extracts cookies and the video URL.
5.  Uses `yt-dlp` (embedded in Python) to download the video using the extracted cookies.

## Verification Plan

### Automated Tests
- None (Hard to automate testing for external auth-walled sites without credentials).

### Manual Verification
1.  **Install Dependencies**: Run `pip install -r requirements.txt`.
2.  **Run Script**: Run `python3 panopto_downloader.py`.
3.  **Test Flow**:
    - Paste a Panopto video URL when prompted.
    - Log in to the university portal in the opened browser window.
    - Verify that the video starts downloading and saves to the local directory.
