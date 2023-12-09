def risk_return_plot(tickers, start_date=None, end_date=None, data=True, log=False):
    if data:
        data_df = pd.DataFrame()

        for ticker in tickers:
            stock_data = yf.download(ticker, start=start_date, end=end_date)['Adj Close']
            data_df[ticker] = stock_data

        data_df = data_df.dropna()

        log_returns = np.diff(np.log(data_df), axis=0)[1:]
        returns = np.exp(np.cumsum(log_returns, axis=0)) - 1

        risk = np.std(log_returns, axis=0) * 1000

        plt.scatter(risk, returns[-1, :])

        for i, ticker in enumerate(tickers):
            plt.text(risk[i], returns[-1, i], ticker, ha='right', va='bottom')

        plt.xlabel("Risk (Standard Deviation)")
        plt.ylabel("Return (%)")
        plt.title("Risk & Return Plot")
        plt.axhline(0, color='black', linestyle='--')
        plt.axvline(0, color='black', linestyle='--')
        plt.legend('', frameon=False)
        plt.show()

    else:
        if log:
            log_returns = np.diff(np.log(tickers), axis=0)[1:]
            returns = np.exp(np.cumsum(log_returns, axis=0)) - 1

            risk = np.std(log_returns, axis=0) * 1000

            plt.scatter(risk, returns[-1, :])

            for i in range(len(tickers)):
                plt.text(risk[i], returns[-1, i], tickers[i], ha='right', va='bottom')

            plt.xlabel("Risk (Standard Deviation)")
            plt.ylabel("Return (%)")
            plt.title("Risk & Return Plot")
            plt.axhline(0, color='black', linestyle='--')
            plt.axvline(0, color='black', linestyle='--')
            plt.legend('', frameon=False)
            plt.show()

# Example usage
risk_return_plot(["AMZN", "GOOGL", "MSFT", "AAPL", "NFLX", "META", "NVDA",
                  "TSLA", "ORCL", "INTC", "TSM", "ASML", "AMD", "QCOM",
                  "MU"], start_date="2023-10-10")
