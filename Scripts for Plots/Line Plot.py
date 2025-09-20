import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def line_plt(y, s=None, e=None):
  
  p = pd.DataFrame()  # Create an empty DataFrame

  # Loop for data extraction & Set up statements for start and end dates
  for ticker in y:
    if s is None and e is None:
      data = yf.download(ticker, start="2007-01-01") # None is defined
    elif e is None:
      data = yf.download(ticker, start=s) # Only start date is defined
    elif s is None:
      data = yf.download(ticker, end=e)  # When only end date is defined
    else:
      data = yf.download(ticker, start=s, end=e) # Both dates are defined
      
    if not data.empty:
      p[ticker] = data[('Close', f'{ticker}')] # Assign tickers
            
    p = p.dropna() # Drop rows with NA values
  
  for column in p.columns:
    plt.figure()  # Create a new figure for each plot
    plt.plot(p[column])
    plt.title(column)
    plt.grid(True, linestyle=":", color="grey")
    plt.xlabel('Trading Days')
    plt.ylabel('Prices')
    plt.show()

line_plt(["UNM", "MSFT", "META", "GOOGL", "AMZN"], s = "2023-01-01")
