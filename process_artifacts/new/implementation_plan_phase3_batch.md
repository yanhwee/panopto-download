# Implementation Plan - Batch Download Support

## Goal
Enable users to download multiple videos in one go by providing a text file containing a list of URLs. This avoids the need to log in repeatedly for each video.

## User Review Required
> [!NOTE]
> The script will now ask: "Enter the Panopto Video URL **or** path to a text file:".
> If a file path is detected (e.g., `urls.txt`), it will switch to batch mode.

## Proposed Changes

### [MODIFY] [panopto_downloader.py](../panopto_downloader.py)

1.  **Refactor `main()`**:
    *   Prompt user for input (URL or File).
    *   Launch browser and perform **one-time login**.
    *   Extract cookies.
    *   Iterate through the list of URLs (or single URL) and call `yt-dlp` for each.

2.  **Logic Flow**:
    ```python
    urls = []
    user_input = input("Enter URL or file path: ")
    if os.path.isfile(user_input):
        with open(user_input) as f:
            urls = [line.strip() for line in f if line.strip()]
    else:
        urls = [user_input]

    driver = login_and_get_driver(urls[0]) # Login using the first URL
    cookies = get_cookies(driver)
    driver.quit() # Close browser after getting cookies

    for url in urls:
        download_video(url, cookies)
    ```

## Verification Plan
1.  Create a `test_urls.txt` with 2 Panopto URLs.
2.  Run the script and provide the file path.
3.  Verify that:
    *   Browser opens only once for login.
    *   Both videos are downloaded sequentially.
