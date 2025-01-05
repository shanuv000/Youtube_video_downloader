# YouTube Downloader

A Python script to list and download YouTube videos with merged audio using `yt-dlp`. This script allows users to select a specific video resolution and automatically merges the best audio track into a single file.

---

## Features

- Displays all available video formats for a YouTube video.
- Allows users to choose their desired resolution (e.g., 1080p, 720p, etc.).
- Automatically downloads and merges the video with the best available audio.
- Saves the downloaded video with the original YouTube video title.

---

## Requirements

- **Python 3.x**: Make sure Python 3.x is installed on your system.
- **yt-dlp**: A modern and powerful YouTube downloader library.
- **FFmpeg**: Required for merging video and audio streams.

---

## Installation

### 1. Clone the Repository

Clone this repository or create your own project folder.

```bash
git clone https://github.com/<your-username>/youtube_downloader.git
cd youtube_downloader
```

### 2. Set Up a Virtual Environment

It's recommended to use a virtual environment for your dependencies:

- **macOS/Linux**:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **Windows**:
  ```cmd
  python -m venv venv
  venv\Scripts\activate
  ```

### 3. Install Dependencies

Install the required libraries in the virtual environment:

```bash
pip install yt-dlp
```

### 4. Install FFmpeg

- **macOS** (using Homebrew):

  ```bash
  brew install ffmpeg
  ```

- **Linux**:

  ```bash
  sudo apt install ffmpeg
  ```

- **Windows**:
  Download and install FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html). Ensure it's added to your system's PATH.

---

## Usage

1. **Run the Script**:

   ```bash
   python download_youtube.py
   ```

2. **Enter the YouTube Video URL**:
   When prompted, paste the URL of the YouTube video.

3. **Choose the Desired Resolution**:
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
├── download_youtube.py   # The main Python script
├── README.md             # Documentation
├── .gitignore            # Ignore unnecessary files like venv/
```

---

## Troubleshooting

### FFmpeg Missing

If you see an error like:

```
ERROR: You have requested merging of multiple formats but ffmpeg is not installed.
```

Make sure FFmpeg is installed and accessible via the system PATH. Follow the instructions in the **Installation** section to resolve this issue.

---

## License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute it as needed.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request and describe your changes.

---

Happy downloading! 🚀

---

This version improves formatting, simplifies instructions, and ensures clarity for all users. Let me know if you’d like to add anything else! 🚀
