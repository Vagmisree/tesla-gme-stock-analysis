import yfinance as yf
import pandas as pd

# Download Tesla stock data
tesla_data = yf.download('TSLA', start='2010-01-01', end='2020-12-31')

# Reset index
tesla_data.reset_index(inplace=True)

# Display first five rows
tesla_data.head()
