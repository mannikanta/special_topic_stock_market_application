import requests
import json
import pandas as pd, numpy as np, yfinance as yf, streamlit as st
import plotly.express as plotly

st.title("Stock Dashboard")

if "ticker_name" not in st.session_state:
    st.session_state["ticker_name"] = ""

tickerName = st.text_input("Input any stock's ticker name here", st.session_state["ticker_name"])
submit = st.button("Submit")
if submit:
    st.session_state["ticker_name"] = tickerName;
    st.write("You have entered: ",tickerName)

