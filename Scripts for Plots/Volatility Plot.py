import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def volatility_plt(x):
  
  x = np.log(x / x.shift(1)).dropna() * 100
  
  for column in x.columns:
        plt.figure()  # Create a new figure for each plot
        plt.plot(x[column])
        plt.title(f"{column} Volatility")
        plt.xlabel('Trading Days')
        plt.ylabel('Return (%)')
        plt.show()
        
volatility_plt(result)
