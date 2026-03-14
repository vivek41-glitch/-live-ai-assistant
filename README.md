# 🛰️ Live AI Assistant

A real-time AI assistant that searches the web live and answers your questions instantly — powered by **Groq**, **Tavily**, and **LangChain**.

---

## 🚀 Demo
> Ask anything — get real-time answers with sources!

---

## 🧠 How It Works
```
User Question
     ↓
Tavily searches the web live
     ↓
Results passed to Groq LLM as context
     ↓
Answer returned with sources
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| LangChain | Chain building |
| Groq (LLaMA 3.3) | LLM - super fast inference |
| Tavily | Live web search API |
| Streamlit | UI |
| Python | Backend |

---

## 📁 Project Structure
```
live-ai-assistant/
│
├── assistant.py     → Core logic (LangChain + Groq + Tavily)
├── app.py           → Streamlit UI
├── requirements.txt → Dependencies
├── .gitignore       → Ignores .env file
└── README.md
```

---

## ⚙️ Setup Locally

### 1. Clone the repo
```bash
git clone https://github.com/vivek41-glitch/live-ai-assistant.git
cd live-ai-assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create `.env` file
```
GROQ_API_KEY=your_groq_key_here
TAVILY_API_KEY=your_tavily_key_here
```

Get keys from:
- Groq → https://console.groq.com
- Tavily → https://app.tavily.com

### 4. Run the app
```bash
streamlit run app.py
```

---

## 🔑 API Keys Required

- **Groq** — Free at https://console.groq.com
- **Tavily** — Free tier (1000 calls/month) at https://app.tavily.com

---

## 💡 This vs RAG

| My RAG Project | This Project |
|----------------|--------------|
| PDF → chunks → Vector DB | Web search → live results |
| Static data | Real-time data |
| Retriever fetches chunks | Tavily fetches live pages |
| LLM answers from docs | LLM answers from web |

Same LangChain chain concept — different data source!

---

## 👨‍💻 Built By
**Vivek** — 2nd year CS student passionate about AI/ML
- GitHub: [@vivek41-glitch](https://github.com/vivek41-glitch)
