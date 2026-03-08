import streamlit as st
import os
import asyncio
import yfinance as yf
import pandas as pd

from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient


# -----------------------------
# LOAD ENV VARIABLES
# -----------------------------

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")


# -----------------------------
# GROQ MODEL CLIENT
# -----------------------------

model_client = OpenAIChatCompletionClient(
    model="llama-3.1-8b-instant",
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
    model_info={
        "vision": False,
        "function_calling": False,
        "json_output": False,
        "family": "llama",
        "max_input_tokens": 8192,
        "max_output_tokens": 1024
    }
)


# -----------------------------
# AGENTS
# -----------------------------

stock_agent = AssistantAgent(
    name="StockAnalyst",
    model_client=model_client,
    system_message="""
You are a professional stock analyst.
Analyze company fundamentals, recent performance, and market position.
"""
)

risk_agent = AssistantAgent(
    name="RiskAnalyst",
    model_client=model_client,
    system_message="""
You are a financial risk analyst.
Explain volatility, economic risks, and investment risks.
"""
)

decision_agent = AssistantAgent(
    name="DecisionAgent",
    model_client=model_client,
    system_message="""
Based on stock analysis and risk analysis,
recommend BUY, HOLD, or SELL with reasoning.
"""
)


# -----------------------------
# STOCK DATA FUNCTION
# -----------------------------

def get_stock_data(ticker):

    stock = yf.Ticker(ticker)

    hist = stock.history(period="1mo")

    info = stock.info

    summary = {
        "company": info.get("longName"),
        "sector": info.get("sector"),
        "price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE")
    }

    return hist, summary


# -----------------------------
# AGENT WORKFLOW
# -----------------------------

async def analyze_stock(ticker):

    hist, summary = get_stock_data(ticker)

    data_text = f"""
Company: {summary['company']}
Sector: {summary['sector']}
Current Price: {summary['price']}
Market Cap: {summary['market_cap']}
PE Ratio: {summary['pe_ratio']}
"""

    analysis = await stock_agent.run(
        task=f"Analyze this stock data:\n{data_text}"
    )

    risk = await risk_agent.run(
        task=f"Evaluate the investment risk for this stock:\n{data_text}"
    )

    decision = await decision_agent.run(
        task=f"""
Stock Analysis:
{analysis.messages[-1].content}

Risk Analysis:
{risk.messages[-1].content}

Give final investment recommendation.
"""
    )

    return (
        hist,
        analysis.messages[-1].content,
        risk.messages[-1].content,
        decision.messages[-1].content
    )


# -----------------------------
# STREAMLIT UI
# -----------------------------

st.title("📈 AI Stock Analyzer Agent")

ticker = st.text_input("Enter Stock Ticker (Example: AAPL)")

if st.button("Analyze Stock"):

    hist, analysis, risk, decision = asyncio.run(analyze_stock(ticker))

    st.subheader("Stock Price (Last Month)")
    st.line_chart(hist["Close"])

    st.subheader("📊 Stock Analysis")
    st.write(analysis)

    st.subheader("⚠️ Risk Analysis")
    st.write(risk)

    st.subheader("💡 Investment Decision")
    st.write(decision)