import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import yt_dlp

import tempfile

def get_cookies_from_browser(login_url):
    print("\nLaunching browser... Please log in to your institution's page if prompted.")
    print("The script will wait for you to navigate to the video page.")

    # Setup Chrome options
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # Commented out so user can see and login
    
    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(login_url)

        # Wait for user to login and the video to load
        print("\nACTION REQUIRED: Log in in the browser window.")
        input("Press Enter here once the video page is fully loaded and you can see the player...")

        # Get cookies from the browser
        selenium_cookies = driver.get_cookies()
        user_agent = driver.execute_script("return navigator.userAgent;")
        
        return selenium_cookies, user_agent

    finally:
        driver.quit()

def create_netscape_cookie_file(selenium_cookies):
    """Writes selenium cookies to a temp file in Netscape format."""
    fd, path = tempfile.mkstemp(suffix=".txt", text=True)
    with os.fdopen(fd, 'w') as f:
        f.write("# Netscape HTTP Cookie File\n")
        for cookie in selenium_cookies:
            # Netscape format: domain, flag, path, secure, expiration, name, value
            domain = cookie.get('domain', '')
            # The flag is TRUE if the domain starts with a dot
            flag = "TRUE" if domain.startswith('.') else "FALSE"
            path_str = cookie.get('path', '/')
            secure = "TRUE" if cookie.get('secure') else "FALSE"
            expiry = str(int(cookie.get('expiry', time.time() + 3600)))
            name = cookie.get('name', '')
            value = cookie.get('value', '')
            
            f.write(f"{domain}\t{flag}\t{path_str}\t{secure}\t{expiry}\t{name}\t{value}\n")
    return path

def download_video(url, cookie_file, user_agent):
    print(f"\n[Downloading] {url}")
    
    # Create videos directory if it doesn't exist
    output_dir = "videos"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        ydl_opts = {
            'cookiefile': cookie_file,
            'http_headers': {
                'User-Agent': user_agent
            },
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
            'format': 'best',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download complete!")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def main():
    print("--- Panopto Video Downloader ---")
    
    # Check for command line arguments
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
        print(f"Using input from command line: {user_input}")
    else:
        user_input = input("Enter the Panopto Video URL OR path to a text file (e.g., urls.txt): ").strip()

    if not user_input:
        print("Error: No input provided.")
        return

    urls = []
    if os.path.isfile(user_input):
        print(f"Reading URLs from file: {user_input}")
        with open(user_input, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
        if not urls:
            print("Error: File is empty.")
            return
    else:
        # Basic validation to prevent crashing on "a"
        if not user_input.startswith(('http://', 'https://')):
             print("Error: Invalid URL. Please provide a full URL starting with http:// or https://")
             return
        urls = [user_input]

    print(f"Found {len(urls)} video(s) to download.")

    # 1. Log in once using the first URL
    cookie_file_path = None
    try:
        cookies, user_agent = get_cookies_from_browser(urls[0])
        # Create a temp cookie file
        cookie_file_path = create_netscape_cookie_file(cookies)
        print("\nCookies extracted and secured. Starting batch download...")
    except Exception as e:
        print(f"Login failed: {e}")
        return

    # 2. Download all videos
    try:
        for i, url in enumerate(urls):
            print(f"\nProcessing {i+1}/{len(urls)}...")
            download_video(url, cookie_file_path, user_agent)
    finally:
        # Cleanup temp file
        if cookie_file_path and os.path.exists(cookie_file_path):
            os.remove(cookie_file_path)

    print("\nAll tasks finished.")

if __name__ == "__main__":
    main()
