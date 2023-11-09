import requests
import json
import pandas as pd, numpy as np, yfinance as yf, streamlit as st
import plotly.express as px

url = 'https://yfinance-stock-market-data.p.rapidapi.com/news'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-RapidAPI-Key': 'fda283bdf9mshf6a6fc0eb76274cp193063jsnf0981bc9a1d4',
    'X-RapidAPI-Host': 'yfinance-stock-market-data.p.rapidapi.com'
}

ticker = st.session_state["ticker_name"]
print("*****************************************************************************")
print(ticker)
print("*****************************************************************************")
data = {
    'symbol': ticker
}

# Send the POST request
response = requests.post(url, headers=headers, data=data)
output=""
status = False
# Check if the request was successful
if response.status_code == 200:
    output =response.text
    status = True
elif response.status_code == 400:
    output = "please enter correct ticker name for any stock"
    status = False

else:
    print(f"Request failed with status code: {response.status_code}")
    status = False
    print(response.text)

st.title("News")
if status:
    json_data = json.loads(output)
    length = len(json_data["data"])
    for i in json_data["data"]:
        link = i["link"]
        st.write(link)
