import pandas as pd
import datetime
import matplotlib.pyplot as plt
from adtk.data import validate_series
from adtk.visualization import plot
from adtk.detector import *
from sklearn.ensemble import IsolationForest

import seaborn as sns  # Import Seaborn

data = pd.read_excel(r'D:\SpecialTopicProject1\resources\stock_data.xlsx')

# Convert the 'Date' column to a datetime and set it as the index
data['Date'] = pd.to_datetime(data['Date'] / 1000, unit='s')
data.set_index('Date', inplace=True)


def calculatepricechange(prices):
    return (prices - prices.shift(1)) / prices.shift(1);

priceDifference = calculatepricechange(data[['Closing Price']])



