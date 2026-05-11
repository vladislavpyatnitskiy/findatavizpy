import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import probplot
import pandas as pd
import yfinance as yf

def qq_plot(x, s=None, e=None, log=False):
    p = pd.DataFrame()

    for ticker in x:
        if s is None and e is None:
            data = yf.download(ticker, start="2007-01-01", auto_adjust=True)
        elif e is None:
            data = yf.download(ticker, start=s, auto_adjust=True)
        elif s is None:
            data = yf.download(ticker, end=e, auto_adjust=True)
        else:
            data = yf.download(ticker, start=s, end=e, auto_adjust=True)

        if not data.empty:
            # Safely extract Close regardless of column structure
            close = data['Close']
            if isinstance(close, pd.DataFrame):
                close = close.iloc[:, 0]
            p[ticker] = close

    p = p.dropna()

    # Compute returns 
    if log:
        p = np.log(p / p.shift(1)).dropna()
    else:
        p = (p / p.shift(1) - 1).dropna() * 100

    for column in p.columns:
        fig, ax = plt.subplots()
        probplot(p[column], plot=ax)
        ax.get_lines()[1].set(color='red', linewidth=2)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_title(f"{column} Q-Q Plot")
        plt.tight_layout()
        plt.show()

qq_plot(["AIG", "MET", "HIG", "UNM", "OMF"], s="2023-10-01", log=True)
