import yfinance as yf
import pandas as pd

# Fetch historical stock data from Yahoo Finance
def fetch_stock_data(symbol, start_date, end_date):
    ticker = yf.Ticker(symbol) #We use the yfinance library to 
    return ticker.history(period='1d', start=start_date, end=end_date)


if __name__ == "__main__":
    # Define stock symbol and date range
    SYMBOL = input("What stock would you like to track: ")
    START_DATE = input("What is the start date (yyyy-mm-dd): ")
    END_DATE = input("What is the end date (yyyy-mm-dd): ")
    
    df = fetch_stock_data(SYMBOL, START_DATE, END_DATE)
    print(df)

