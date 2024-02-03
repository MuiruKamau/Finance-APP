import streamlit as st
import yfinance as yf

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Nvidia! 
""")
# Define the ticker symbol
tickerSymbol = 'NVDA'
# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2023-1-1', end='2024-2-3')
# Open High Low Close Volume Dividends Stock Splits
st.write("""
## Closing Price
""")

import plotly.express as px

fig = px.line(tickerDf, x=tickerDf.index, y='Close', title='Stock Closing Price')
st.plotly_chart(fig)

# Calculate the percentage change in closing price
percentage_change = (tickerDf.Close[-1] - tickerDf.Close[0]) / tickerDf.Close[0] * 100

st.write(f"Percentage Change: {percentage_change:.2f}%")
st.write("""
## Volume Price
""")

fig_volume = px.line(tickerDf, x=tickerDf.index, y='Volume', title='Stock Volume')
st.plotly_chart(fig_volume)


  