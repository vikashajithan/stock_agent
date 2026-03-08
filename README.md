# 📈 AI Stock Analyzer Agent

An **Agentic AI system** that analyzes stock market data using multiple AI agents.
The application uses **AutoGen, Groq LLM, and Streamlit** to simulate a collaborative AI workflow for stock analysis and investment decision-making.

This project demonstrates how **AI agents can work together to analyze financial data and generate investment insights**.

---

# 🚀 Project Overview

The system takes a **stock ticker symbol** as input and performs the following steps:

1. Fetches real-time stock data using **Yahoo Finance API**
2. Uses multiple AI agents to analyze the stock
3. Provides investment insights and a recommendation

The result is a **simple AI-powered stock analysis tool**.

---

# 🧠 Agent Workflow

This project uses **three AI agents** working together.

```text
User Input (Stock Ticker)
        │
        ▼
Stock Analyst Agent
(Analyzes company fundamentals)
        │
        ▼
Risk Analyst Agent
(Evaluates investment risks)
        │
        ▼
Decision Agent
(Recommends BUY / HOLD / SELL)
```

---

# 🤖 Agents in the System

### 1️⃣ Stock Analyst Agent

Analyzes:

* Company fundamentals
* Market position
* Business performance

### 2️⃣ Risk Analyst Agent

Evaluates:

* Market volatility
* Economic risks
* Investment uncertainty

### 3️⃣ Decision Agent

Combines the previous analyses and recommends:

* **BUY**
* **HOLD**
* **SELL**

---

# 🏗️ Tech Stack

* **Python**
* **AutoGen Framework**
* **Groq LLM (llama-3.1-8b-instant)**
* **Streamlit**
* **Yahoo Finance API**
* **uv (fast Python package manager)**

---

# 📂 Project Structure

```text
Stock_agent/
│
├── main.py          # Streamlit application
├── .env             # Environment variables
├── pyproject.toml   # Project dependencies
├── uv.lock          # Dependency lock file
└── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/stock-agent.git
cd stock-agent
```

---

### 2️⃣ Install dependencies

Using **uv**

```bash
uv sync
```

Or using pip

```bash
pip install streamlit pyautogen autogen-ext openai tiktoken yfinance pandas python-dotenv
```

---

# 🔑 Environment Variables

Create a `.env` file in the project directory.

```text
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run the Application

```bash
uv run streamlit run main.py
```

Open the app in your browser:

```text
http://localhost:8501
```

---

# 📊 Example Output

Input:

```text
Stock Ticker: AAPL
```

Output:

```text
Stock Analysis:
Apple has strong fundamentals with consistent revenue growth.

Risk Analysis:
Moderate risk due to market volatility and global economic factors.

Investment Decision:
HOLD – strong company but valuation is already high.
```

---

# 🎯 Key Concepts Demonstrated

* Multi-Agent AI Systems
* Agentic Workflow Design
* LLM-based Financial Analysis
* Real-time Data Integration
* Streamlit AI Applications

---

# 🔮 Future Improvements

Potential upgrades for this project:

* Technical indicator analysis (RSI, MACD)
* Financial news sentiment analysis
* Portfolio recommendation agent
* Multi-agent trading strategies
* Historical performance comparison

---

# 👨‍💻 Author

**Vikash Ajithan**

Exploring **Generative AI, AI Agents, and Autonomous Systems**

GitHub: https://github.com/vikashajithan

---

⭐ If you found this project useful, consider giving it a star!
