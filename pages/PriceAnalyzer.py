import pandas as pd
import streamlit as st
import requests
import datetime
import json
import os
import plotly.express as px
import matplotlib.pyplot as plt
from adtk.data import validate_series
from adtk.visualization import plot
from adtk.detector import *
from sklearn.ensemble import IsolationForest

directory_path = r"D:\SpecialTopicProject1\resources"

st.title("Stock Price Dashboard")
period = st.sidebar.text_input('Period')


priceDeflection = st.sidebar.number_input('deflection',min_value=-0.05, max_value=0.05)



url = 'https://yfinance-stock-market-data.p.rapidapi.com/price'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-RapidAPI-Key': '68c481dc34msh9d4aa1fbf0b453fp1d5ab1jsn020820feca65',
    'X-RapidAPI-Host': 'yfinance-stock-market-data.p.rapidapi.com'
}

ticker = st.session_state["ticker_name"]
data = {
    'symbol': ticker,
    'period': period,
}

response = requests.post(url, headers=headers, data=data)
json_data = json.loads(response.text)

data_length = json_data.get("data", [])
data_list = []

if data_length:
    for item in data_length:
        # Create a dictionary with the data
        child_attributes = {
            "Closing Price": item.get("Close", None),
            "Date": item.get("Date", None),
            "Day High": item.get("High", None),
            "Day Low": item.get("Low", None),
            "Opening Price": item.get("Open", None),
            "Volume": item.get("Volume", None),
        }
        data_list.append(child_attributes)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data_list)

if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# Save the DataFrame to an Excel file in the specified directory
excel_file_path = os.path.join(directory_path, "stock_data.xlsx")
df.to_excel(excel_file_path, index=False)

# Provide a message indicating the file was saved successfully
st.write(f"Excel file saved at: {excel_file_path}")

data = pd.read_excel(r'D:\SpecialTopicProject1\resources\stock_data.xlsx')

# Select the 'Date' and 'Closing Price' columns
selected_column = data[['Date', 'Closing Price']]
# selected_column.set_index(selected_column['Date'], inplace=True)
selected_column['Date'] = pd.to_datetime(selected_column['Date']/ 1000,unit='s')

def calculatepricechange(prices):
    return (prices - prices.shift(1)) / prices.shift(1);

# Calculate price difference
selected_column['PriceDifference'] =  calculatepricechange(data[['Closing Price']])


if int(priceDeflection)>-0.05 or int(priceDeflection)<0.05:
    result = selected_column[selected_column['PriceDifference'] > priceDeflection][['Date', 'PriceDifference']]
    fig = px.scatter(result, x='Date', y='PriceDifference', title=ticker)
    st.write(fig)
else:
    print("something wrong")

fig1 = px.line(selected_column, x=selected_column['Date'], y = data['Closing Price'], title=ticker)
st.write(fig1)


