import streamlit as st
from datetime import datetime
from assistant import ask
import pytz


# ---- Page Config ----
st.set_page_config(
    page_title="Live AI Assistant",
    page_icon="🛰️",
    layout="centered"
)

# ---- Custom CSS ----
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Inter:wght@300;400;500&display=swap');

* { font-family: 'Inter', sans-serif; }

.stApp { background: #0a0a0f; color: #e0e0e0; }

h1 {
    font-family: 'Space Mono', monospace !important;
    font-size: 2rem !important;
    color: #00ff88 !important;
}

.datetime-bar {
    background: #111118;
    border: 1px solid #2a2a3a;
    border-radius: 8px;
    padding: 0.6rem 1rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.85rem;
    color: #00ff88;
    margin-bottom: 1.5rem;
}
.stTextInput > div > div > input {
    background: #111118 !important;
    border: 1px solid #2a2a3a !important;
    border-radius: 8px !important;
    color: #e0e0e0 !important;
    font-size: 1rem !important;
    caret-color: #00ff88 !important;
    -webkit-text-fill-color: #e0e0e0 !important;
} 
.stTextInput > div > div > input:focus {
    border-color: #00ff88 !important;
}

.stButton > button {
    background: #00ff88 !important;
    color: #0a0a0f !important;
    font-family: 'Space Mono', monospace !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 8px !important;
    width: 100% !important;
}

.answer-box {
    background: #111118;
    border: 1px solid #2a2a3a;
    border-left: 3px solid #00ff88;
    border-radius: 8px;
    padding: 1.5rem;
    margin-top: 1.5rem;
    font-size: 0.95rem;
    line-height: 1.7;
    color: #d0d0d0;
}

.source-tag {
    display: inline-block;
    background: #1a1a2a;
    border: 1px solid #2a2a3a;
    border-radius: 4px;
    padding: 2px 8px;
    font-size: 0.75rem;
    color: #888;
    margin: 4px 4px 0 0;
    font-family: 'Space Mono', monospace;
}

.history-item {
    border-bottom: 1px solid #1a1a2a;
    padding: 1rem 0;
}

.history-q {
    color: #00ff88;
    font-size: 0.85rem;
    font-family: 'Space Mono', monospace;
    margin-bottom: 0.4rem;
}

.history-a {
    color: #888;
    font-size: 0.85rem;
    line-height: 1.5;
}
</style>
""", unsafe_allow_html=True)

# ---- Header ----
st.markdown("# 🛰️LIVE AI ASSISTANT")
st.markdown("Real-time web search powered by Tavily + Groq")

# ---- Date & Time Bar ----

IST = pytz.timezone("Asia/Kolkata")
now = datetime.now(IST)

st.markdown(f"""
<div class="datetime-bar">
    📅 {now.strftime('%B %d, %Y')} &nbsp;&nbsp; 🕐 {now.strftime('%I:%M %p')}
</div>
""", unsafe_allow_html=True)

# ---- Session History ----
if "history" not in st.session_state:
    st.session_state.history = []

# ---- Input ----
question = st.text_input("", placeholder="Ask anything... e.g. Latest AI news today")
search_btn = st.button("🔍 SEARCH")

# ---- On Search ----
if search_btn and question.strip():
    with st.spinner("🌐 Searching the web..."):
        result = ask(question)

    # Answer
    st.markdown(f'<div class="answer-box">{result["answer"]}</div>', unsafe_allow_html=True)

    # Sources
    if result["sources"]:
        st.markdown("<br>**Sources:**", unsafe_allow_html=True)
        for src in result["sources"]:
            st.markdown(f'<span class="source-tag">🔗 {src}</span>', unsafe_allow_html=True)

    # Save to history
    st.session_state.history.insert(0, {
        "q": question,
        "a": result["answer"][:200] + "..." if len(result["answer"]) > 200 else result["answer"]
    })

elif search_btn and not question.strip():
    st.warning("Please enter a question!")

# ---- History ----
if st.session_state.history:
    st.markdown("---")
    st.markdown("**Recent Searches:**")
    for item in st.session_state.history[:5]:
        st.markdown(f"""
        <div class="history-item">
            <div class="history-q">▸ {item['q']}</div>
            <div class="history-a">{item['a']}</div>
        </div>
        """, unsafe_allow_html=True)