import pandas as pd, numpy as np, yfinance as yf, streamlit as st
import plotly.express as px

st.title("Stock Dashboard")
ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')
submitButton = st.sidebar.button('download data')
# yf.ticker
data = yf.download(ticker, start_date,end_date,submitButton)


print(data)


try:
    with open('D:/SpecialTopicProject1/resources/data.txt', 'w') as f:
        f.write(data.to_string())
except FileNotFoundError:
    print("The 'docs' directory does not exist")


fig = px.line(data, x=data.index, y = data['Adj Close'], title=ticker)
st.plotly_chart(fig)

pricing_data, fundamental_data, news = st.tabs(["Pricing Data","Fundamental Data", "Top 10 News"])

with pricing_data:
    st.header('Price Movement')
    data2 = data;
    data2['% change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
    st.write(data2)

    annual_return = data2['% change'].mean()*252*100
    st.write('Annual Return is ', annual_return,'%')

with fundamental_data:
    # info = data.get('companyOfficers');
    st.write(data)

with news:
    st.write('Top 10 news')

