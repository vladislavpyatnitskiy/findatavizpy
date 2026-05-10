import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

def several_cml_rets(x, s=None, e=None, title=None):
  
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
  
  p = (np.exp(np.cumsum(np.log(p / p.shift(1)).dropna())) - 1) * 100
   
  plt.figure(figsize=(10, 6))
     
  plt.plot(p, label=x)
  plt.title(title)
  plt.xlabel('Trading Days')
  plt.ylabel('Return (%)')
  plt.legend()
  plt.grid(True)
  plt.show()

several_cml_rets(
  ["AIG", "MET", "HIG", "UNM", "OMF"], 
  s="2023-10-01", title="Performance of Insurance Stocks"
)
