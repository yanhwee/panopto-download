import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import yt_dlp

def main():
    print("--- Panopto Video Downloader ---")
    video_url = input("Enter the Panopto Video URL: ").strip()

    if not video_url:
        print("Error: No URL provided.")
        return

    print("\nLaunching browser... Please log in to your institution's page if prompted.")
    print("The script will wait for you to navigate to the video page.")

    # Setup Chrome options
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # Commented out so user can see and login
    
    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(video_url)

        # Wait for user to login and the video to load
        # We'll check for a specific element or just wait for a manual confirmation?
        # A simple robust way is to ask the user to press Enter in the console once the video is visible.
        print("\nACTION REQUIRED: Log in in the browser window.")
        input("Press Enter here once the video page is fully loaded and you can see the player...")

        # Get cookies from the browser
        selenium_cookies = driver.get_cookies()
        
        # Convert cookies to a format yt-dlp accepts (Netscape format or dict)
        # yt-dlp accepts a dict of key-value pairs in the 'cookiefile' option, 
        # but passing them directly via 'http_headers' or using a cookie jar is better.
        # Actually, yt-dlp can take cookies as a simple key=value string in headers 
        # or we can construct a cookie jar.
        
        # Let's try to pass cookies to yt-dlp.
        # The easiest way programmatically is often to save them to a file or format them for the 'cookies' param if supported,
        # but yt-dlp python embedding supports a 'cookiefile'. 
        # We can also pass 'http_headers' with 'Cookie'.
        
        cookie_header = "; ".join([f"{c['name']}={c['value']}" for c in selenium_cookies])
        
        print("\nCookies extracted. Starting download...")
        
        # yt-dlp options
        ydl_opts = {
            'http_headers': {
                'Cookie': cookie_header,
                'User-Agent': driver.execute_script("return navigator.userAgent;")
            },
            'outtmpl': '%(title)s.%(ext)s',
            'format': 'best',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        print("\nDownload complete!")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
