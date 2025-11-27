# Panopto Video Downloader

<img src="logo.png" width="200" alt="Panopto Downloader Logo">

A simple, robust tool to download Panopto videos using your university credentials. It leverages Selenium for authentication and `yt-dlp` for high-quality video downloading.

## Features
- **Browser-based Login**: Handles SSO and 2FA by letting you log in via a real Chrome window.
- **High Quality**: Uses `yt-dlp` to download the best available stream.
- **Simple**: Just paste the URL and go.

## Prerequisites
- **Google Chrome** installed on your machine.
- **Python 3** installed.

## Installation

1.  **Clone or Download** this repository.
2.  **Navigate** to the folder in your terminal.
3.  **Set up a virtual environment** (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```
4.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Activate your virtual environment** (if not already active):
    ```bash
    source venv/bin/activate
    ```
2.  **Run the script**:
    *   **Interactive Mode**:
        ```bash
        python3 panopto_downloader.py
        ```
    *   **Direct URL**:
        ```bash
        python3 panopto_downloader.py "https://panopto.com/..."
        ```
    *   **Batch File**:
        ```bash
        python3 panopto_downloader.py urls.txt
        ```
3.  **Follow the on-screen instructions**:
    - **Single Video**: Paste the Panopto Video URL.
    - **Batch Download**: Paste the path to a text file (e.g., `urls.txt`) containing one URL per line.
    - A Chrome window will open. **Log in** to your institution's portal.
    - Navigate to the video page so the player is visible.
    - Return to the terminal and press **Enter**.
    - The script will download all videos in the list using the same login session.

## Research Journey
This project explored multiple approaches, including a Chrome Extension and Native Messaging. You can read about why we settled on this Python solution in [JOURNEY.md](JOURNEY.md).

## Development Process
This tool was built with the help of **Antigravity**, an AI agent. You can view the artifacts generated during the development process in the `process_artifacts/` directory:
- `task.md`: The task list and progress tracking.
- `implementation_plan.md`: The initial technical plan.
- `walkthrough.md`: The user guide generated during verification.

## Author Notes

My first time trying out Google Antigravity!

It’s rather good! It took a single prompt (i.e. download panapto videos for school) to generate a minimal working product. The resulting code is not overly complex (which is a good point), but it’s the automation of research and coding that is invaluable and executed really well.

It provides useful artefacts that walkthroughs its research and coding process, which were extremely useful for me since I had no prior idea on how to begin this project initially. It served as a highly efficient researcher and coder, rapidly exploring various ideas I had vaguely in mind.

A downside is that the agentic flow isn’t perfect yet. I had to manually intervene during some debugging (specially chrome extension issues) and it quickly degrades back to the cumbersome back-and-forth of a pure-conversational AI.

Compared to other agentic tools (like Gemini CLI / Code Assist), Antigravity feels more polished and useful. It produces a nice agentic workflow interface for developers to clearly understand what it’s doing, and it feels noticeably faster.

Overall I think Antigravity would speed up a lot of research-coding work for product development. It can also generate images like icons, though I haven’t tested it for UI mockups yet.

No rate limits were encountered during this project’s development.
- Conversation mode: Planning
- Model: Gemini 3 Pro (low)