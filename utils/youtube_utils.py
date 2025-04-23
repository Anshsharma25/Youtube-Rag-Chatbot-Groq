from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    """Fetch the transcript of a YouTube video using its video ID.

    Args:
        video_id (str): The ID of the YouTube video.

    Returns:
        list: A list of dictionaries containing the transcript segments.
    """
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([d['text'] for d in transcript_list])
    return full_text

