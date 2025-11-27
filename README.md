# Panopto Video Downloader

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
    ```bash
    python3 panopto_downloader.py
    ```
3.  **Follow the on-screen instructions**:
    - Paste the Panopto Video URL when prompted.
    - A Chrome window will open. **Log in** to your institution's portal.
    - Navigate to the video page so the player is visible.
    - Return to the terminal and press **Enter**.
    - The video will download to the current directory.

## Development Process
This tool was built with the help of **Antigravity**, an AI agent. You can view the artifacts generated during the development process in the `process_artifacts/` directory:
- `task.md`: The task list and progress tracking.
- `implementation_plan.md`: The initial technical plan.
- `walkthrough.md`: The user guide generated during verification.

## Author Notes

My first time trying out Google Antigravity!

Beyond expectations. All it took was a single prompt (i.e. download panapto videos for school) for it to generate a working product (at the very least). The code doesn’t look complex (which is also a good point), but it’s the research work that was completely automated and executed well. I wonder how the simpler Gemini CLI (agent mode) stacks up against this. I used another prompt to package the product up, i.e. generate README and explicitly ask it to transfer its process artefacts for showcase purposes.

Overall, saved me so much research time to build this.