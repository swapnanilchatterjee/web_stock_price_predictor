import streamlit as st
import pandas as pd
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime

# Title and stock input
st.title("Stock Price Predictor App")
stock = st.text_input("Enter the stock ID", "AMZN")

# Date range
end = datetime.now()
start = datetime(end.year - 29, end.month, end.day)

# Load data
amazon_data = yf.download(stock, start, end)
model = load_model("Latest_stock_price_model.keras")

# Display stock data
st.subheader("Stock Data")
st.write(amazon_data)

# Split data
splitting_len = int(len(amazon_data) * 0.7)
x_test = pd.DataFrame(amazon_data.Close[splitting_len:])

# Plotting function
def plot_graph(figsize, values, full_data, extra_data=0, extra_dataset=None):
    fig = plt.figure(figsize=figsize)
    plt.plot(values, 'Orange')
    plt.plot(full_data.Close, 'b')
    if extra_data:
        plt.plot(extra_dataset, 'green')
    return fig

# Plot moving averages
st.subheader('Original Close Price and MA for 250 days')
amazon_data['MA_for_250_days'] = amazon_data.Close.rolling(250).mean()
st.pyplot(plot_graph((15, 6), amazon_data['MA_for_250_days'], amazon_data, 0))

st.subheader('Original Close Price and MA for 200 days')
amazon_data['MA_for_200_days'] = amazon_data.Close.rolling(200).mean()
st.pyplot(plot_graph((15, 6), amazon_data['MA_for_200_days'], amazon_data, 0))

st.subheader('Original Close Price and MA for 100 days')
amazon_data['MA_for_100_days'] = amazon_data.Close.rolling(100).mean()
st.pyplot(plot_graph((15, 6), amazon_data['MA_for_100_days'], amazon_data, 0))

st.subheader('Original Close Price and MA for 100 days and MA for 250 days')
st.pyplot(plot_graph((15, 6), amazon_data['MA_for_100_days'], amazon_data, 1, amazon_data['MA_for_250_days']))

# Scale data
scaler = MinMaxScaler(feature_range=(0, 1))
scaler_data = scaler.fit_transform(x_test[['Close']])
x_data = []
y_data = []

# Prepare data for prediction
for i in range(100, len(scaler_data)):
    x_data.append(scaler_data[i-100:i])
    y_data.append(scaler_data[i])

# Convert lists to NumPy arrays
x_data = np.array(x_data)
y_data = np.array(y_data)

# Make predictions
predictions = model.predict(x_data)
inv_pre = scaler.inverse_transform(predictions)
inv_y_test = scaler.inverse_transform(y_data)

# Prepare plotting data
plotting_data = pd.DataFrame(
    {
        'original_test_data': inv_y_test.reshape(-1),
        'predictions': inv_pre.reshape(-1)
    },
    index=amazon_data.index[splitting_len+100:]
)

# Display plotting data
st.subheader("Original Close price vs Predicted Close price")
st.write(plotting_data.head())

# Plot the results
st.subheader('Original Close Price vs Predicted Close Price')
fig = plt.figure(figsize=(15, 6))
plt.plot(pd.concat([amazon_data.Close[:splitting_len+100], plotting_data['original_test_data']], axis=0))
plt.plot(pd.concat([amazon_data.Close[:splitting_len+100], plotting_data['predictions']], axis=0))
plt.legend(["Data - not used", "Original Test data", "Predicted Test data"])
st.pyplot(fig)
