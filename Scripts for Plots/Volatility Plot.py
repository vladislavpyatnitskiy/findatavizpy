import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

def volatility_plt(x, s=None, e=None):
  
  p = pd.DataFrame()  # Create an empty DataFrame

  # Loop for data extraction & Set up statements for start and end dates
  for ticker in x:
    if s is None and e is None:
      data = yf.download(ticker, start="2007-01-01")
    elif e is None:
      data = yf.download(ticker, start=s) 
    elif s is None:
      data = yf.download(ticker, end=e) 
    else:
      data = yf.download(ticker, start=s, end=e)

    if not data.empty:
      p[ticker] = data[('Close', f'{ticker}')]
            
  p = p.dropna() # Drop rows with NA values
  
  p = np.log(p / p.shift(1)).dropna() * 100
  
  for column in p.columns:
        plt.figure()  # Create a new figure for each plot
        plt.plot(p[column])
        plt.title(f"{column} Volatility")
        plt.xlabel('Trading Days')
        plt.ylabel('Return (%)')
        plt.grid(True, linestyle=":", color="grey")
        plt.show()
        
volatility_plt(["AIG", "MET", "HIG", "UNM", "OMF"], s="2023-10-01")
