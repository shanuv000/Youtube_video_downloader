import yt_dlp


def list_video_formats(url):
    """
    Lists all available video formats for the given YouTube URL.

    Args:
        url (str): The YouTube video URL.

    Returns:
        list: A list of available video formats.
    """
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        # Extract video information without downloading
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [])

        print("\nAvailable video formats:")
        for f in formats:
            if f.get('vcodec') != 'none':  # Show only video formats
                print(f"{f['format_id']} - {f['ext']} - {f['height']
                                                         }p - {f['fps']}fps - {f['vcodec']}")

        return formats


def download_video_with_audio(url, format_id):
    """
    Downloads the video in the specified format and merges it with the best audio.

    Args:
        url (str): The YouTube video URL.
        format_id (str): The format ID of the video to download.
    """
    ydl_opts = {
        # Combine the chosen video format and best audio
        'format': f'{format_id}+bestaudio/best',
        'merge_output_format': 'mp4',            # Ensure the final file is in MP4 format
        # Save the file with the video title
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("\nDownloading video...")
        ydl.download([url])
        print("Download completed!")


if __name__ == "__main__":
    # Prompt the user for the YouTube video URL
    video_url = input("Enter the YouTube video URL: ").strip()

    # Step 1: List available formats
    formats = list_video_formats(video_url)

    # Step 2: Prompt the user to select a format
    chosen_format = input(
        "\nEnter the format ID of the resolution you want to download (e.g., '137' for 1080p): ").strip()

    # Step 3: Download the selected video format with audio
    download_video_with_audio(video_url, chosen_format)
