def get_relevant_chunk(vectorstore, query, k=4):
    """Retrieve the most relevant chunk from the vector store based on the query.

    Args:
        vectorstore (FAISS): The FAISS vector store object.
        query (str): The query string to search for.
        k (int): The number of top results to return.

    Returns:
        list: A list of dictionaries containing the most relevant chunks.
    """
    return vectorstore.similarity_search(query, k=k)