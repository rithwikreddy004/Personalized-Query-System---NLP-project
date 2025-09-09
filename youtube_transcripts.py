# youtube_transcripts.py
from youtube_transcript_api import YouTubeTranscriptApi

def fetch_youtube_transcript(video_url):
    """Fetch and return the transcript from the YouTube video."""
    video_id = video_url.split("v=")[-1]
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        content = ' '.join([item['text'] for item in transcript])
        return content
    
    except Exception as e:
        return f"Error fetching transcript: {e}"
