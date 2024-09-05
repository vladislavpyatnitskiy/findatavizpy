import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# Function to create barplot
def bar_plt(tickers, start_date=None, end_date=None, col="blue", main=None,
            data=False):
    data_list = []

    if data:
        for ticker in tickers:
            if start_date is None and end_date is None:
                stock_data = yf.download(ticker)
            elif start_date is None:
                stock_data = yf.download(ticker, end=end_date)
            elif end_date is None:
                stock_data = yf.download(ticker, start=start_date)
            else:
                stock_data = yf.download(ticker,start=start_date,end=end_date)

            data_list.append(stock_data['Adj Close'].pct_change().dropna())

        tickers = [ticker.upper() for ticker in tickers]
        x = np.sort([np.exp(np.sum(np.diff(np.log(col))[-1])) - 1 for col in data_list])[::-1]
    else:
        x = np.sort([0] * len(tickers))[::-1]

    # Barplot
    bar_plt_script = plt.barh(range(len(x)), x, color=col)
    plt.yticks(range(len(x)), tickers)
    plt.title(main)
    plt.ylabel("Data Source: Yahoo Finance")
    
    # Add grey dotted lines
    for idx, bar in enumerate(bar_plt_script):
        plt.axhline(y=bar.get_width(), color="grey", linestyle="--")

    plt.show()

# Test
bar_plt(["AIG", "MET", "HIG", "UNM", "OMF"], start_date="2023-10-01",
        main="Asset Performance", data=True)
