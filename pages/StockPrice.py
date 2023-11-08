import pandas as pd, numpy as np, yfinance as yf, streamlit as st
import plotly.express as px
import requests
import json


st.title("Stock Price Dashboard")
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')


url = 'https://yfinance-stock-market-data.p.rapidapi.com/price-customdate'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-RapidAPI-Key': '68c481dc34msh9d4aa1fbf0b453fp1d5ab1jsn020820feca65',
    'X-RapidAPI-Host': 'yfinance-stock-market-data.p.rapidapi.com'
}

# ticker = st.sidebar.text_input('Ticker')
ticker = st.session_state["ticker_name"]
print("*****************************************************************************")
print(ticker)
print("*****************************************************************************")
data = {
    'symbol': ticker,
    'start' : start_date,
    'end' : end_date
}

# Send the POST request
response = requests.post(url, headers=headers, data=data)


# yf.ticker
json_data = json.loads(response.text)
print(len(json_data["data"]))

# fig = px.line(response.text, x=data.index, y = data['Adj Close'], title=ticker)
# st.plotly_chart(fig)
