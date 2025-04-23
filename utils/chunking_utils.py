from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_text(text):
    """Chunk the text into smaller segments using Langchain's RecursiveCharacterTextSplitter.

    Args:
        text (str): The text to be chunked.

    Returns:
        list: A list of dictionaries containing the chunked text segments.
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size = 500 , chunk_overlap = 50)
    return splitter.split_text(text)