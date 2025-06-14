import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Load financial data
df = pd.read_csv("data/processed/financial_data.csv")

# Streamlit dashboard
st.title("Real-time Financial Dashboard")

# Line chart of stock price
st.subheader("Stock Price Trend")
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Close Price')
plt.legend()
st.pyplot(plt)

# AI-Powered Financial Summary using Ollama
st.subheader("AI-Generated Financial Summary")
prompt = f"Analyze the following financial data:\n{df.to_string()}"

ollama_url = "http://localhost:11434/api/generate"
payload = {
    "model": "tim2nearfield/finance",
    "prompt": prompt,
    "stream": False
}
response = requests.post(ollama_url, json=payload)
if response.ok:
    summary = response.json().get("response", "No summary generated.")
else:
    summary = "Failed to get response from Ollama."

st.write(summary)