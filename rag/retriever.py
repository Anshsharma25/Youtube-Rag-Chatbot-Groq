from langchain.schema import Document

def get_relevant_chunks(vectorstore, query: str, k: int = 4) -> list[Document]:
    """Retrieve the top k similar chunks for the query."""
    return vectorstore.similarity_search(query, k=k)