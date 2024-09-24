import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def several_cml_rets(x, title=None): # Cumulative Returns of Stocks
  
  x = (np.exp(np.cumsum(np.log(x / x.shift(1)).dropna())) - 1) * 100
  
  plt.figure(figsize=(10, 6))
    
  for column in x.columns:
    plt.plot(x.index, x[column], label=column)
    plt.title(title)
    plt.xlabel('Trading Days')
    plt.ylabel('Return (%)')
    plt.legend()
    plt.grid(True)
    plt.show()

several_cml_rets(result, title="Performance of Insurance Stocks")
