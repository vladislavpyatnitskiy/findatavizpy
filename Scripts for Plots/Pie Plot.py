import matplotlib.pyplot as plt

def pie_plt(slices, tickers, main=None, sub=None):
    colors = plt.cm.rainbow(range(len(tickers)))
    plt.pie(slices,
            labels=[f'{ticker} {round(slice_/sum(slices)*100,
                                      2)}%' for ticker,
                    slice_ in zip(tickers, slices)],
            autopct='%1.1f%%')
    plt.title(main)
    plt.show()

# Test
pie_plt(slices=[0.278716291651169, 0.411679570881108, 0.0727978571595576,
                0.176817615423501, 0.0599886648846643],
        tickers=["BELU", "BSPB", "IRAO", "LKOH", "RTKM"],
        main="Dividend Yield Distribution")
