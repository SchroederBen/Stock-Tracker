import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetch historical stock data from Yahoo Finance
def fetch_stock_data(symbol, start_date, end_date):
    ticker = yf.Ticker(symbol)
    return ticker.history(period='1d', start=start_date, end=end_date)

# Calculate moving averages
def calculate_moving_averages(dataframe, window_short=50, window_long=200):
    dataframe['MA_short'] = dataframe['Close'].rolling(window=window_short).mean()
    dataframe['MA_long'] = dataframe['Close'].rolling(window=window_long).mean()
    return dataframe

# Visualize stock data with moving averages
def plot_stock_data(dataframe, symbol):
    plt.figure(figsize=(14, 7))
    plt.plot(dataframe['Close'], label='Close Price')
    plt.plot(dataframe['MA_short'], label='50-Day Moving Average')
    plt.plot(dataframe['MA_long'], label='200-Day Moving Average')
    plt.title(f'{symbol} Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Define stock symbol and date range
    SYMBOL = 'AAPL'
    START_DATE = '2020-01-01'
    END_DATE = '2021-01-01'
    
    # Fetch, calculate, and plot
    df = fetch_stock_data(SYMBOL, START_DATE, END_DATE)
    df = calculate_moving_averages(df)
    plot_stock_data(df, SYMBOL)
