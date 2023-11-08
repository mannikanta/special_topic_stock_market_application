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
# # print("=====================================================")
# # print(selected_column.dtypes)
# # print("=====================================================")
# # Convert the 'Date' column to a pandas DatetimeIndex
# # selected_column['Date'] = selected_column['Date'].apply(
# #      lambda timestamp: pd.to_datetime(datetime.datetime.fromtimestamp(timestamp / 1e3)).strftime('%Y-%m-%d')
# #     # lambda timestamp: pd.to_datetime(datetime.datetime.fromtimestamp(timestamp / 1e3),unit='s')
# # )
selected_column.set_index(selected_column['Date'], inplace=True)
selected_column['Date'] = pd.to_datetime(selected_column['Date']/ 1000,unit='s')
selected_column['Date'] = pd.DatetimeIndex(selected_column['Date'])

# # print("=====================================================")
# # print(selected_column.dtypes)
# # print("=====================================================")
# #
# #
# # quantile_detector = QuantileAD(low=0.01, high=0.99)
# # anomalies = quantile_detector.fit_detect(selected_column['Date'])
# # plot(selected_column, anomaly= anomalies, anomaly_color= "red",anomaly_tag="Marker")
# # plt.show()
#
#
# Fit an Isolation Forest model
clf = IsolationForest(contamination=0.05, random_state=0)  # You can adjust the contamination parameter
selected_column['anomaly_score'] = clf.fit_predict(selected_column[['Closing Price']])
print(selected_column)
#
# # Create a scatter plot to visualize anomalies
# plt.figure(figsize=(12, 6))
# plt.scatter(selected_column['Date'], selected_column['Closing Price'], c=selected_column['anomaly_score'], cmap='viridis')
# plt.xlabel('Date')
# plt.ylabel('Closing Price')
# plt.title('Anomaly Detection using Isolation Forest')
# plt.colorbar()
# plt.show()
#
# # fig = px.line(selected_column, x=plt.xlabel('Date'), y= plt.ylabel('Closing Price'), title=ticker)
#
# # fig = px.line(selected_column, x=selected_column['Date'], y = selected_column['Closing Price'], title=ticker)
# # st.plotly_chart(fig)
#
#


