import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def drawdown_plt(y, s=None, e=None):
  
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
  
  x = np.log(p / p.shift(1)).dropna() * 100
  
  x[x > 0] = 0
  
  for column in x.columns:
        plt.figure()  # Create a new figure for each plot
        plt.plot(x[column])
        plt.title(f"{column} Drawdown")
        plt.grid(True, linestyle=":", color="grey")
        plt.axhline(y=0, color="black")
        plt.xlabel('Trading Days')
        plt.ylabel('Negative Return (%)')
        plt.show()
        
drawdown_plt(["AAPL", "MSFT", "META", "GOOGL", "AMZN"], s = "2023-01-01")
