from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from utils.youtube_utils import get_transcript  
from utils.chunking_utils import chunk_text
from utils.embeddings_utils import create_vectorstore
from rag.retriever import get_relevant_chunks
from rag.groq_llm import get_groq_response
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='static')
CORS(app)  # This allows all origins. You can specify which domains to allow.

# Function to extract video ID from YouTube URL
def extract_video_id_from_url(url):
    """
    Extracts the video ID from a YouTube URL.
    This function works for both standard YouTube URLs and shortened URLs.
    """
    # Check for the full URL format: https://www.youtube.com/watch?v=video_id
    if 'youtu.be' in url:
        # Shortened URL (e.g., https://youtu.be/video_id)
        video_id = url.split('/')[-1]
    elif 'youtube.com' in url:
        # Full URL (e.g., https://www.youtube.com/watch?v=video_id)
        video_id = url.split('v=')[-1]
        if '&' in video_id:
            video_id = video_id.split('&')[0]
    else:
        raise ValueError("Invalid YouTube URL")
    
    return video_id

@app.route('/')
def index():
    # Serve the index.html page when the user visits the root URL
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    video_input = data.get('video_input')
    query = data.get('query')

    try:
        # Extract video ID if needed (from URL or directly passed)
        video_id = extract_video_id_from_url(video_input) if 'http' in video_input else video_input

        # Fetch transcript and process it
        transcript = get_transcript(video_id)
        chunks = chunk_text(transcript)
        vs = create_vectorstore(chunks)
        docs = get_relevant_chunks(vs, query)
        answer = get_groq_response(query, docs)
        
        return jsonify({'response': answer})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
