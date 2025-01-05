Here's a well-structured `README.md` for your YouTube Downloader project:

````markdown
# YouTube Downloader

A Python script to list and download YouTube videos with merged audio using `yt-dlp`. This script allows users to select a specific video resolution and automatically merges the best audio track.

---

## Features

- Lists all available video formats for a YouTube video.
- Allows users to select their desired resolution (e.g., 1080p, 720p, etc.).
- Automatically downloads and merges video and audio into a single file.
- Saves the downloaded video with the title of the YouTube video.

---

## Requirements

- **Python 3.x**: Make sure Python 3.x is installed.
- **yt-dlp**: For downloading videos and managing formats.
- **ffmpeg**: Required for merging video and audio streams.

---

## Installation

### 1. Clone the Repository

Clone the project repository or create a Python project directory.

### 2. Create and Activate Virtual Environment

- **macOS/Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
````

- **Windows**:
  ```cmd
  python -m venv venv
  venv\Scripts\activate
  ```

### 3. Install Dependencies

Install the required libraries in your virtual environment:

```bash
pip install yt-dlp
```

Install `ffmpeg`:

- **macOS** (using Homebrew):
  ```bash
  brew install ffmpeg
  ```
- **Linux**:
  ```bash
  sudo apt install ffmpeg
  ```
- **Windows**:
  Download and install FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html).

---

## Usage

1. **Run the Script**:

   ```bash
   python download_youtube.py
   ```

2. **Enter the YouTube Video URL**:
   When prompted, paste the URL of the YouTube video.

3. **Select the Desired Resolution**:
   The script will display all available video formats. Enter the format ID (e.g., `137` for 1080p).

4. **Download and Merge**:
   The script will download the video and merge it with the best available audio.

---

## Example Output

```bash
Enter the YouTube video URL: https://www.youtube.com/watch?v=EXAMPLE_ID

Available video formats:
137 - mp4 - 1080p - 30fps - avc1.640028
136 - mp4 - 720p - 30fps - avc1.4d401f
135 - mp4 - 480p - 30fps - avc1.4d401e
134 - mp4 - 360p - 30fps - avc1.4d4015

Enter the format ID of the resolution you want to download (e.g., '137' for 1080p): 137

Downloading video...
[download] Destination: Video_Title.mp4
[download] 100% of 50.00MiB in 00:10
Download completed!
```

---

## Folder Structure

```plaintext
youtube_downloader/
├── venv/                 # Virtual environment (not tracked in Git)
├── download_youtube.py   # The main script
├── README.md             # Documentation
├── .gitignore            # Ignore unnecessary files
```

---

## License

This project is licensed under the **MIT License**. Feel free to use and modify it as needed.

---

## Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository.
2. Create a new feature branch.
3. Submit a pull request.

---

## Troubleshooting

### FFmpeg Missing

If you see an error like:

```
ERROR: You have requested merging of multiple formats but ffmpeg is not installed.
```

Ensure FFmpeg is installed and accessible via the system path.

---
