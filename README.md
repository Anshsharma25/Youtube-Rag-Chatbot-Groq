<!-- # Youtube-Rag-Chatbot-Groq -->
### README.md
# YouTube Transcript Chatbot using RAG and Groq

A fast and intelligent chatbot that answers questions based on any YouTube video’s transcript using Retrieval-Augmented Generation (RAG), FAISS vector search, and open-source LLMs served via Groq.

## Features
- **Transcript Extraction**: Automatically fetches YouTube video transcripts (with fallback to auto-generated Hindi if English is unavailable).
- **Chunking**: Splits transcripts into semantically coherent chunks for better retrieval.
- **Vector Store**: Uses FAISS for efficient similarity search over transcript embeddings.
- **RAG Response**: Retrieves relevant chunks and generates answers using Groq-hosted open-source LLMs (e.g., Mixtral).
- **Debugging**: Prints all chunks and top-k retrieved documents for transparency.

## Prerequisites
- Python 3.8+
- A Groq API key (create an account at https://console.groq.com/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/youtube-rag-chatbot-groq.git
   cd youtube-rag-chatbot-groq
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\\Scripts\\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set your Groq API key in `.env`:
   ```dotenv
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

1. Open `main.py` and set the desired YouTube `video_id` and `query`.
2. Run the script:
   ```bash
   python main.py
   ```
3. View debug output:
   - **ALL CHUNKS**: Lists every transcript chunk.
   - **TOP-K DOCUMENTS**: Shows the top retrieved chunks for your query.
4. The final **Response** is printed below the debug logs.

## Project Structure
```
├── README.md
├── requirements.txt
├── .env
├── main.py
├── utils/
│   ├── youtube_utils.py
│   ├── chunking_utils.py
│   └── embeddings_utils.py
└── rag/
    ├── __init__.py
    ├── retriever.py

https://github.com/user-attachments/assets/ddaa036a-be41-45b3-a952-92fb74eaabf0


    └── groq_llm.py
```

## Customization
- **Model Selection**: In `rag/groq_llm.py`, change `model_name` to any supported Groq model from your console.
- **Chunk Size**: Adjust `chunk_size` and `chunk_overlap` in `utils/chunking_utils.py`.
- **Top-K Retrieval**: Modify `k` in `get_relevant_chunks` to return more or fewer document chunks.

<video controls src="Youtube chatbot.mp4" title="Title"></video>



https://github.com/user-attachments/assets/8d579ec2-ee5e-46cd-83c1-fd96b2aae5c7


