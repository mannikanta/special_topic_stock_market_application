# import requests
# import streamlit as st
#
#
# def generateResponse():
#         url = 'https://yfinance-stock-market-data.p.rapidapi.com/stock-info'
#         headers = {
#             'Content-Type': 'application/x-www-form-urlencoded',
#             'X-RapidAPI-Key': 'fda283bdf9mshf6a6fc0eb76274cp193063jsnf0981bc9a1d4',
#             'X-RapidAPI-Host': 'yfinance-stock-market-data.p.rapidapi.com'
#         }
#
#         # ticker = st.sidebar.text_input('Ticker')
#         ticker = st.session_state["ticker_name"]
#         print("*****************************************************************************")
#         print(ticker)
#         print("*****************************************************************************")
#         data = {
#             'symbol': ticker
#         }
#
#         # Send the POST request
#         response = requests.post(url, headers=headers, data=data)
#         return response;
#
#
