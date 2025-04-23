

from utils.youtube_utils import get_transcript
from utils.chunking_utils import chunk_text
from utils.embeddings_utils import create_vectorstore
# from rag import get_relevant_chunks
from rag.retriever import get_relevant_chunks
from rag.groq_llm import get_groq_response

if __name__ == "__main__":
    # video_id = "X0btK9X0Xnk"

    # Example video ID
    video_id =  "i51KM08yQzM" 
    query = "Ravan kon tha ?"

    # Step 1: Retrieve transcript
    transcript = get_transcript(video_id)

    # Step 2: Chunk transcript
    chunks = chunk_text(transcript)

    # # Debug: Print all chunks
    # print("=== ALL CHUNKS ===")
    # for idx, chunk in enumerate(chunks):
    #     print(f"[{idx}] {chunk}")


    # Step 3: Create vectorstore and retrieve relevant chunks
    vs = create_vectorstore(chunks)
    docs = get_relevant_chunks(vs, query)

    # Debug: Print top-k retrieved documents
    print("=== TOP-K DOCUMENTS ===")
    for idx, doc in enumerate(docs):
        print(f"[{idx}] {doc.page_content}")

    # Step 4: Generate response
    response = get_groq_response(query, docs)




    print("\nResponse:\n", response)