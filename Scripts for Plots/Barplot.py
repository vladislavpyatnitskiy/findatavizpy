import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def bar_plt(y, s=None, e=None, col="blue", main=None): # Bar plot
  
    p = pd.DataFrame()  # Create an empty DataFrame

    # Loop for data extraction & Set up statements for start and end dates
    for ticker in y:
        if s is None and e is None:
            # When neither start date nor end date is defined
            data = yf.download(ticker, start="2007-01-01")
        elif e is None:
            data = yf.download(ticker, start=s) # Only start date is defined
        elif s is None:
            data = yf.download(ticker, end=e)  # When only end date is defined
        else:
            # When both start date and end date are defined
            data = yf.download(ticker, start=s, end=e)

        # Extract the Adjusted Close prices and add to the DataFrame
        if not data.empty:
            p[ticker] = data[('Close', f'{ticker}')]
            
    p = p.dropna() # Drop rows with NA values

    x = ((np.exp(np.sum(np.log(p / p.shift(1)).dropna())) - 1) * 100)
        
    x = pd.DataFrame(x)
        
    x.columns = ['Return']
  
    x = x.sort_values(by = 'Return')
    
    x.plot(kind='bar')
    plt.title(main)
    plt.grid(True, linestyle=":", color="grey")
    plt.show()
    
bar_plt(["AIG", "MET", "HIG", "UNM", "OMF"], s="2023-10-01",
        main='Performance of Insurance Companies (%)') # Test
