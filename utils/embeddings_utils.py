from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


def create_vectorstore(chunks):
    """Create a FAISS vector store from the given chunks using HuggingFaceEmbeddings.

    Args:
        chunks (list): A list of dictionaries containing the chunked text segments.

    Returns:
        FAISS: A FAISS vector store object.
    """
    embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(chunks, embedding=embedder)
    return vectorstore