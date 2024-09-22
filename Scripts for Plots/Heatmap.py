import yfinance as yf
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def heat_map(y, s=None, e=None): # Heatmap
  
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
  
    x = np.log(p / p.shift(1)).dropna() # Returns
    M = x.corr() # Correlation Matrix
  
    plt.figure(figsize=(10, 8)) # Create the heatmap
    sns.heatmap(M, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Stock Returns Correlation Heatmap') # Add labels and title
    plt.show() # Show
    
heat_map(["XOM", "UNM", "GOOGL", "VIRT"], s = "2023-01-01") # Test
