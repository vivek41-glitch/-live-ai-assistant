import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langchain_core.prompts import ChatPromptTemplate
from datetime import datetime

# Load keys
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY") or st.secrets.get("TAVILY_API_KEY")

# ---- LLM: Groq ----
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)

# ---- Tool: Tavily Search ----
search = TavilySearch(max_results=4, tavily_api_key=TAVILY_API_KEY)

# ---- Prompt ----
prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant with access to real-time web search results.
Answer the user's question clearly and concisely using the context below.
If the context doesn't have enough info, say so honestly.

Context from web search:
{context}

User Question:
{question}

Answer:
""")

# ---- Chain ----
chain = prompt | llm

# ---- Main Function ----
def ask(question: str) -> dict:
    # Step 1: Search web
    raw_results = search.invoke(question)

    # Step 2: Extract content and sources
    context_parts = []
    sources = []

    results_list = raw_results.get("results", [])
    for r in results_list:
        content = r.get("content", "")
        url = r.get("url", "")
        if content:
            context_parts.append(content)
        if url:
            domain = url.split("/")[2] if "//" in url else url
            sources.append(domain)

    context = "\n\n".join(context_parts)

    # Step 3: Pass to chain
    response = chain.invoke({
        "context": context,
        "question": question
    })

    return {
        "answer": response.content,
        "sources": list(set(sources))
    }


# ---- Quick Test ----
if __name__ == "__main__":
    now = datetime.now()
    print(f"📅 Date: {now.strftime('%B %d, %Y')}")
    print(f"🕐 Time: {now.strftime('%I:%M %p')}")
    print("-" * 40)

    result = ask("What is the latest news in AI today?")
    print("ANSWER:", result["answer"])
    print("\nSOURCES:", result["sources"])
