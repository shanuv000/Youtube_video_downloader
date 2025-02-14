from flask import Flask, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

# Create a downloads directory if it doesn't exist
DOWNLOADS_DIR = os.path.join(os.getcwd(), "downloads")
if not os.path.exists(DOWNLOADS_DIR):
    os.makedirs(DOWNLOADS_DIR)


@app.errorhandler(400)
def bad_request(error):
    """Custom handler for 400 errors."""
    return jsonify({'error': 'Bad Request', 'message': str(error)}), 400


@app.errorhandler(500)
def internal_server_error(error):
    """Custom handler for 500 errors."""
    return jsonify({'error': 'Internal Server Error', 'message': str(error)}), 500


@app.route('/')
def home():
    return "Welcome to the YouTube Downloader API! 🚀 Use /list-formats and /download endpoints to interact with the service."


@app.route('/list-formats', methods=['POST'])
def list_formats():
    try:
        data = request.json
        video_url = data.get('url')

        if not video_url:
            return jsonify({'error': 'URL is required'}), 400

        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            formats = info_dict.get('formats', [])
            available_formats = [
                {
                    'format_id': f['format_id'],
                    'ext': f['ext'],
                    'height': f.get('height', 'N/A'),
                    'fps': f.get('fps', 'N/A'),
                    'vcodec': f.get('vcodec', 'N/A')
                } for f in formats if f.get('vcodec') != 'none'
            ]
            return jsonify({'formats': available_formats})

    except yt_dlp.utils.DownloadError as e:
        return jsonify({'error': 'Invalid YouTube URL or video unavailable', 'message': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Failed to list formats', 'message': str(e)}), 500


@app.route('/download', methods=['POST'])
def download_video():
    try:
        data = request.json
        video_url = data.get('url')
        format_id = data.get('format_id')

        if not video_url or not format_id:
            return jsonify({'error': 'Both URL and format_id are required'}), 400

        ydl_opts = {
            'format': f'{format_id}+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(DOWNLOADS_DIR, '%(title)s.%(ext)s'),
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        return jsonify({'message': 'Download completed!', 'file_path': DOWNLOADS_DIR})

    except yt_dlp.utils.DownloadError as e:
        return jsonify({'error': 'Failed to download video', 'message': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
