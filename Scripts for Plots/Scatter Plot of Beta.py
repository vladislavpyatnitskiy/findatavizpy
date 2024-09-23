import numpy as np
import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def beta_plt(y, i = "^GSPC", s=None, e=None):
    
    y.append(i)
    
    p = pd.DataFrame()  # Create an empty DataFrame

    # Loop for data extraction & Set up statements for start and end dates
    for ticker in y:
        if s is None and e is None: 
            # When neither start date nor end date is defined
            data = yf.download(ticker)
        elif e is None:
            data = yf.download(ticker, start=s) # Only start date is defined
        elif s is None:
            data = yf.download(ticker, end=e)  # When only end date is defined
        else:
            # When both start date and end date are defined
            data = yf.download(ticker, start=s, end=e)

        # Extract the Adjusted Close prices and add to the DataFrame
        if not data.empty:
            p[ticker] = data['Adj Close']

    p = p.dropna() # Drop rows with NA values
    p = np.log(p / p.shift(1)).dropna() # Returns
    
    y.remove(i)
    
    stocks = p[y] # Data Frame with Stocks values
    index = p[i] # Column with Index values
    
    for column in stocks.columns:
      plt.figure()  # Create a new figure for each plot
      plt.scatter(x = index, y = stocks[column])
      plt.legend('', frameon = False)
      sns.regplot(x = index, y = stocks[column], line_kws={"color": "red"})
      plt.title(f"{column} Beta Plot")
      plt.xlabel(f"{i} Return (%)")
      plt.ylabel(f"{column} Return (%)")
      plt.show()
    
beta_plt(y=["UNM", "OMF"], i = "^GSPC", s="2022-01-01") # Test
