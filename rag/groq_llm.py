import os
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()

# Use a supported Groq model; 'mixtral-8x7b-32768' is deprecated.
# Recommended replacement: 'mistral-7b' or another current model.
llm = ChatGroq(
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="gemma2-9b-it"  # or another supported model from your Groq console
)

def get_groq_response(query, docs):
    context = "\n".join([doc.page_content for doc in docs])
    prompt = f"Answer the following question using only the context below:\n\nContext:\n{context}\n\nQuestion: {query}\n"
    # Using invoke instead of deprecated __call__
    return llm.invoke([HumanMessage(content=prompt)]).content