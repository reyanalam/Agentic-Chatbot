# Agentic Chatbot with Phidata + Groq

An intelligent multi-agent chatbot built using [Phidata](https://docs.phidata.com/) and powered by Groq's blazing-fast LLMs. This chatbot includes two specialized agents:
-  `WebSearchAgent`: Performs real-time web searches.
-  `FinanceAgent`: Provides financial data such as stock prices, analyst recommendations, and company news.

## Tech Stack

- **Framework**: [Phidata](https://docs.phidata.com/)
- **LLM Provider**: [Groq](https://groq.com/)
- **Search Tool**: DuckDuckGo
- **Finance Tool**: Yahoo Finance (via `YFinanceTools`)
- **Local Server**: FastAPI via Uvicorn

---

## Features

### Web Search Agent
- Uses **DuckDuckGo** to search for up-to-date information.
- Displays responses in **Markdown** format.
- **Always includes sources** for transparency.

### Finance Agent
- Uses **YFinanceTools** to fetch:
  - Stock Prices
  - Latest Company News
  - Analyst Recommendations
  - Company Info
- Automatically formats outputs into **tables** for readability.

### Multi-AI Agent
- Combines both agents into a single unified interface.
- Smartly delegates tasks based on the query.
- Ensures rich, informative responses with both **data** and **context**.

---

## Example Query

```python
multi_ai_agent.print_response(
    "Summarize the latest news about Tesla and its stock price",
    stream=True
)
```
## Running the Playground Locally

### 1. Clone the repository

```
git clone https://github.com/your-username/agentic-chatbot.git
cd agentic-chatbot
```

### 2. Set up the environment

Create a .env file with the following variables
```
GROQ_API_KEY=your_groq_api_key
API_KEY=your_phi_api_key
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Run the playgroung

```
python playground.py
```

Login to phidata and open phidata dashboard. Add the endpoint and run it to interact with the agentic chatbot


## Contact

1. **Linkedin:** https://www.linkedin.com/in/reyanalam/
2. **Gmail:** reyanalam115@gmail.com
