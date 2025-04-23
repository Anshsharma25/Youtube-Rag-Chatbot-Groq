from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound

def get_transcript(video_id, languages=["en"]):
    """
    Retrieve the transcript for a YouTube video, trying the specified languages first,
    then falling back to Hindi auto-generated if necessary.
    """
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
    except NoTranscriptFound:
        # Fallback to Hindi auto-generated
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["hi"])
    full_text = " ".join([d['text'] for d in transcript_list])
    return full_text