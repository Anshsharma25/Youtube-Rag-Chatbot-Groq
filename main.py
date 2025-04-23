

from utils.youtube_utils import get_transcript
from utils.chunking_utils import chunk_text
from utils.embeddings_utils import create_vectorstore
# from rag import get_relevant_chunks
from rag.retriever import get_relevant_chunks
from rag.groq_llm import get_groq_response

if __name__ == "__main__":
    # video_id = "X0btK9X0Xnk"
    video_id = "ZFb-W1PAcnI"  # Example video ID
    query = "how can we do bajrang bhand?"

    transcript = get_transcript(video_id)
    chunks = chunk_text(transcript)
    vs = create_vectorstore(chunks)
    docs = get_relevant_chunks(vs, query)
    response = get_groq_response(query, docs)

    print("\nResponse:\n", response)

