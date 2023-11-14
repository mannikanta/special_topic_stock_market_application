import requests
import json
import pandas as pd, numpy as np, yfinance as yf, streamlit as st
import plotly.express as px

url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules'
headers = {
    # 'Content-Type': 'application/x-www-form-urlencoded',
    'X-RapidAPI-Key': '68c481dc34msh9d4aa1fbf0b453fp1d5ab1jsn020820feca65',
    'X-RapidAPI-Host': 'yahoo-finance15.p.rapidapi.com'
}

# ticker = st.sidebar.text_input('Ticker')
ticker = st.session_state["ticker_name"]
print("*****************************************************************************")
print(ticker)
print("*****************************************************************************")
querystring = {"ticker":ticker,"module":"asset-profile"}

# Send the POST request
response = requests.get(url, headers=headers,  params=querystring)
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

st.title("About")
if status:
    json_data = json.loads(output)
    st.write("Ticker Name :   ",ticker)
    st.write("Business Type :  ",json_data["body"]["industry"])
    st.write("Phone Number :   ", json_data["body"]["phone"], "     Website : ", json_data["body"]["website"])
    st.write("Business Summary :  ",json_data["body"]["longBusinessSummary"])
    # fig = px.line(output, title=ticker)
    # st.plotly_chart(fig)
else:
    st.write(output)


# try:
#     with open('D:/SpecialTopicProject1/resources/data.txt', 'w') as f:
#         f.write(response.text)
# except FileNotFoundError:
#     print("The 'docs' directory does not exist")