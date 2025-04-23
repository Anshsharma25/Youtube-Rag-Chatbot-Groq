import os 
from langchain.chat_models import ChatGroq
from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    temperature=0.7,
    model_name="mixtral-8x7b-32768",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def get_groq_response(query, docs):                     
    """Generate a response from the Groq LLM based on the query and context.

    Args:
        query (str): The query string to search for.
        context (str): The context string to provide additional information.

    Returns:
        str: The generated response from the Groq LLM.
    """
    # Combine the context from the documents into a single string
    context = "\n".join([doc.page_content for doc in docs])
    prompt = f"Answer the following question using only the context below:\n\nContext:\n{context}\n\nQuestion: {query}\n"
    return llm([HumanMessage(content=prompt)]).content