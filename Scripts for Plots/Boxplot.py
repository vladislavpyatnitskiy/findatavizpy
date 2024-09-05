import yfinance as yf
import matplotlib.pyplot as plt

# Function to create boxplot
def box_plt(tickers, start_date=None, end_date=None, main=None,
            log_scale=False):
    data = []
    
    for ticker in tickers:
        if start_date is None and end_date is None:
            stock_data = yf.download(ticker)
        elif start_date is None:
            stock_data = yf.download(ticker, end=end_date)
        elif end_date is None:
            stock_data = yf.download(ticker, start=start_date)
        else:
            stock_data = yf.download(ticker, start=start_date, end=end_date)
        
        data.append(stock_data['Adj Close'])
    
    data = [d.dropna() for d in data if not d.empty] # Get rid of NA
    
    tickers = [ticker.upper() for ticker in tickers]
    
    if log_scale or start_date is not None or end_date is not None:
        data = [d.pct_change().dropna() for d in data]
    
    plt.boxplot(data, labels=tickers, vert=True, patch_artist=True, notch=True)
    plt.title(main)
    plt.xlabel("Data Source: Yahoo Finance")
    plt.ylabel("Returns")
    plt.axhline(y=0, color='grey', linestyle='--')
    plt.show()

# Test
box_plt(["AAPL", "MSFT", "META", "GOOGL", "AMZN"], start_date = "2023-01-01",
        main = "Boxplot of IT companies")
