import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def box_plt(y, s=None, e=None, main=None):
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

    x = np.log(p / p.shift(1)).dropna()
     
    x.plot(kind="box")    
    plt.title(main)
    plt.xlabel("Data Source: Yahoo Finance")
    plt.ylabel("Returns")
    plt.grid(True, linestyle=":", color="grey")
    plt.axhline(y=0, color='grey', linestyle='--')
    plt.show()

# Test
box_plt(["AAPL", "MSFT", "META", "GOOGL", "AMZN"], s = "2023-01-01",
        main = "Boxplot of IT companies")
