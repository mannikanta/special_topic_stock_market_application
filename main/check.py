import pandas as pd
import datetime
import matplotlib.pyplot as plt
from adtk.data import validate_series
from adtk.visualization import plot
from adtk.detector import *
from sklearn.ensemble import IsolationForest

import seaborn as sns  # Import Seaborn

# Set the Seaborn style before using the plot function
sns.set_style("dark")

# scikit-learn

data = pd.read_excel(r'D:\SpecialTopicProject1\resources\stock_data.xlsx')

# Convert the 'Date' column to a datetime and set it as the index
data['Date'] = pd.to_datetime(data['Date'] / 1000, unit='s')
data.set_index('Date', inplace=True)

# Select the 'Closing Price' column after setting the index
selected_column = data[['Closing Price']]

quantile_detector = QuantileAD(low=0.01, high=0.99)
anomalies = quantile_detector.fit_detect(selected_column)
# plot.style.use("default")
plot(selected_column, anomaly=anomalies, anomaly_color="red", anomaly_tag="Marker")
plt.show()



# clf = IsolationForest(contamination=1)
# clf.fit(selected_column)
#
# data['Anomaly'] = clf.predict(selected_column)
#
# print(data)











# Convert the 'Date' column to a pandas DatetimeIndex
# selected_column['Date'] = selected_column['Date'].apply(
#     lambda timestamp: datetime.datetime.fromtimestamp(timestamp / 1e3).strftime('%Y-%m-%d')
# )
# selected_column.set_index('Date', inplace=True)  # Set 'Date' as the index
# print(selected_column)
# threshold_detector = ThresholdAD(low=0.25, high=0.75)
# anomalies = threshold_detector.detect(selected_column)
# plot(selected_column, anomaly=anomalies, anomaly_color="red", anomaly_tag="marker")
# plt.show()













# import pandas as pd
# import datetime
# import matplotlib.pyplot as plt
# from adtk.data import validate_series
# from adtk.visualization import plot
# from adtk.detector import *
#
# data = pd.read_excel(r'D:\SpecialTopicProject1\resources\stock_data.xlsx')  # Use pd.read_excel for Excel files
#
# selected_column = data[['Date', 'Closing Price']]
#
# selected_column['Date'] = selected_column['Date'].apply(
#     lambda timestamp: datetime.datetime.fromtimestamp(timestamp / 1e3).strftime('%Y-%m-%d')
# )
#
# threshold_detector = ThresholdAD(low=0.25, high = 0.75)
# anomalies = threshold_detector.detect(selected_column)
# plot(selected_column, anomaly=anomalies,anomaly_color="red",anomaly_tag="marker")
# plt.show()


# import pandas as pd
# import datetime
# import matplotlib.pyplot as plt
# from adtk.data import validate_series
# from adtk.visualization import plot
# from adtk.detector import *
#
# data = pd.read_excel(r'D:\SpecialTopicProject1\resources\stock_data.xlsx')  # Use pd.read_excel for Excel files
# selected_column = data["Date"]
# for x in selected_column:
#     dates = datetime.datetime.fromtimestamp(x / 1e3)
#     formatted_date = dates.strftime('%Y-%m-%d')  # Format as 'YYYY-MM-DD'
#     print(formatted_date)
